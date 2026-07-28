# Exercise Suggestion Microservice

CS361 microservice that returns exercise recommendations over a REST API with JSON.

## Assigned teammates

- Derrick McClain
- Tristin
- Jacob

## Communication pipe

Other programs send HTTP requests to this API. The microservice returns exercise recommendations in JSON format.

### How other programs request data

Send a **GET** request to `/exercises`.

Example:

```bash
curl http://localhost:5001/exercises
curl "http://localhost:5001/exercises?type=cardio&level=beginner"
```

## How to run

1. Python 3.10+
2. From this folder:

```bash
pip install -r requirements.txt
python app.py
```

Service runs on `http://localhost:5001`.

## Project status

Starter scaffold only. Teammates should replace the placeholder response in `app.py` with real recommendation logic.
