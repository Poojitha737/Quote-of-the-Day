# Quote of the Day

Flask web application that displays a random motivational quote. The supplied report describes Git/GitHub, Docker and Jenkins CI/CD.

## Run locally

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
# source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000.

## Docker

```bash
docker build -t quote-app .
docker run -p 5000:5000 quote-app
```
