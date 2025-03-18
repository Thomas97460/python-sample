import json
import re
import sys
import os

def main(input_file, output_file):
    try:
        # Vérifier si le fichier existe et n'est pas vide
        if not os.path.exists(input_file) or os.path.getsize(input_file) == 0:
            with open(output_file, "w") as out:
                out.write("✅ **No vulnerabilities found.** Your dependencies are secure!\n")
            return

        # Charger le contenu JSON
        with open(input_file, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                with open(output_file, "w") as out:
                    out.write(f"Error processing vulnerabilities: Invalid JSON format. Details: {str(e)}\n")
                return
        
        # Créer le fichier de sortie
        with open(output_file, "w") as out:
            out.write("# Dependency Vulnerabilities\n\n")
            
            if not isinstance(data, list) or len(data) == 0:
                out.write("✅ **No vulnerabilities found.** Your dependencies are secure!\n")
                return
            
            out.write(f"⚠️ **Found {len(data)} vulnerabilities** in your dependencies:\n\n")
            out.write("| Package | Installed Version | Vulnerable Version | Vulnerability ID | Description |\n")
            out.write("|---------|-------------------|-------------------|-----------------|-------------|\n")
            
            for vuln in data:
                if "vulnerabilities" not in vuln or not vuln["vulnerabilities"]:
                    continue
                
                for v in vuln["vulnerabilities"]:
                    package = vuln.get("package_name", "Unknown")
                    installed = vuln.get("installed_version", "Unknown")
                    affected = v.get("vulnerable_spec", "Unknown")
                    vuln_id = v.get("vulnerability_id", "Unknown")
                    description = v.get("advisory", "No description available")
                    
                    # Nettoyer la description pour le tableau Markdown
                    description = re.sub(r"\s+", " ", description).strip()
                    description = description[:100] + "..." if len(description) > 100 else description
                    
                    out.write(f"| {package} | {installed} | {affected} | {vuln_id} | {description} |\n")
            
            out.write("\n### Vulnerability severity summary:\n\n")
            out.write("Safety doesn't provide severity information by default in the free version.\n")
    except Exception as e:
        with open(output_file, "w") as out:
            out.write(f"Error processing vulnerabilities: {str(e)}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python format_vulnerabilities.py <input_file> <output_file>")
        sys.exit(1)
    
    main(sys.argv[1], sys.argv[2])
