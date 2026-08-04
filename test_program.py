"""Test program for the Exercise Suggestion Microservice."""
import requests

# Request data from the microservice
response = requests.get(
    "http://localhost:5001/exercises",
    params={
        "muscle_group": "chest",
        "equipment": "dumbbells",
        "difficulty": "beginner",
    },
)

# Receive the data
exercise_data = response.json()

print("Got", exercise_data["count"], "exercises back:")
for exercise in exercise_data["exercises"]:
    print("-", exercise["name"])