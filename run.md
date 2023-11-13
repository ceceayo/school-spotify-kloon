# Hoe deze site te draaien
---
Om de site te runnen heb je Python 3.11 en PIP nodig. Het beste kun je werken in een VENV.
Alle stappen moeten in de `site/spotifykloon` directory uitgevoerd worden.

## Dependencies installeren
```bash
pip install -r requirements.txt
```

## Database installeren
```bash
./manage.py migrate
```

## Server starten
```bash
./manage.py runserver
```
