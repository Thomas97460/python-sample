class DataProcessor:
    def transform_data(self, data):
        """
        Transforme une entrée de données en ajoutant des informations supplémentaires :
        - 'full_name' : concaténation de 'first_name' et 'last_name'
        - 'age_group' : catégorie d'âge basée sur la valeur de 'age'
        
        :param data: dict avec au moins les clés 'first_name', 'last_name' et 'age'
        :return: dict modifié avec les nouvelles clés ajoutées
        """
        new_data = data.copy()
        
        # Construction du nom complet
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        new_data['full_name'] = f"{first_name} {last_name}".strip()
        
        # Détermination du groupe d'âge
        age = data.get('age')
        if isinstance(age, (int, float)):
            if age < 18:
                new_data['age_group'] = 'Minor'
            elif age < 65:
                new_data['age_group'] = 'Adult'
            else:
                new_data['age_group'] = 'Senior'
        else:
            new_data['age_group'] = 'Unknown'
            
        return new_data

    def calculate_statistics(self, ages):
        """
        Calcule quelques statistiques basiques (nombre, minimum, maximum, moyenne) à partir d'une liste d'âges.
        
        :param ages: liste de valeurs numériques représentant des âges
        :return: dict contenant les statistiques calculées
        """
        if not ages:
            return {"count": 0, "min": None, "max": None, "average": None}
        
        count = len(ages)
        min_age = min(ages)
        max_age = max(ages)
        average = sum(ages) / count
        
        return {
            "count": count,
            "min": min_age,
            "max": max_age,
            "average": round(average, 2)
        }

    def filter_records(self, records, field, value):
        """
        Filtre une liste d'enregistrements en fonction d'une clé (field) et d'une valeur donnée.
        Pour les valeurs de type chaîne de caractères, la comparaison est effectuée de manière insensible à la casse.
        
        :param records: liste de dictionnaires
        :param field: clé sur laquelle filtrer
        :param value: valeur attendue pour la clé
        :return: liste des enregistrements qui correspondent aux critères
        """
        filtered = []
        for record in records:
            if field in record:
                record_value = record[field]
                # Comparaison insensible à la casse pour les chaînes
                if isinstance(record_value, str) and isinstance(value, str):
                    if record_value.lower() == value.lower():
                        filtered.append(record)
                else:
                    if record_value == value:
                        filtered.append(record)
        return filtered
