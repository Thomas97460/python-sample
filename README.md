# Python Web Application

A simple web application built with Flask and containerized with Docker.

## Project Structure

```
python-sample/
├── src/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   └── about.html
│   └── static/
│       └── css/
│           └── style.css
├── requirements.txt
├── Dockerfile
└── .github/workflows/
    └── ci.yml
```

## Development Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   cd src
   python app.py
   ```
5. Access the application at http://localhost:5000

## Docker

To build and run with Docker:

```bash
docker build -t python-web-app .
docker run -p 5000:5000 python-web-app
```

## CI/CD

GitHub Actions workflow automatically builds and tests the Docker container when changes are pushed to the main branch.
