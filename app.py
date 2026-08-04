"""Exercise Suggestion Microservice — Flask REST API."""

from flask import Flask, jsonify, request

app = Flask(__name__)

VALID_MUSCLE_GROUPS = {
    "chest",
    "back",
    "legs",
    "arms",
    "shoulders",
    "core",
    "full_body",
}

EXERCISES = [
    {
        "name": "Push-Up",
        "muscle_group": "chest",
        "equipment": "bodyweight",
        "difficulty": "beginner",
    },
    {
        "name": "Dumbbell Bench Press",
        "muscle_group": "chest",
        "equipment": "dumbbells",
        "difficulty": "beginner",
    },
    {
        "name": "Barbell Bench Press",
        "muscle_group": "chest",
        "equipment": "barbell",
        "difficulty": "intermediate",
    },
    {
        "name": "Incline Dumbbell Press",
        "muscle_group": "chest",
        "equipment": "dumbbells",
        "difficulty": "intermediate",
    },
    {
        "name": "Bodyweight Squat",
        "muscle_group": "legs",
        "equipment": "bodyweight",
        "difficulty": "beginner",
    },
    {
        "name": "Goblet Squat",
        "muscle_group": "legs",
        "equipment": "dumbbells",
        "difficulty": "beginner",
    },
    {
        "name": "Barbell Back Squat",
        "muscle_group": "legs",
        "equipment": "barbell",
        "difficulty": "intermediate",
    },
    {
        "name": "Romanian Deadlift",
        "muscle_group": "legs",
        "equipment": "dumbbells",
        "difficulty": "intermediate",
    },
    {
        "name": "Pull-Up",
        "muscle_group": "back",
        "equipment": "bodyweight",
        "difficulty": "intermediate",
    },
    {
        "name": "Dumbbell Row",
        "muscle_group": "back",
        "equipment": "dumbbells",
        "difficulty": "beginner",
    },
    {
        "name": "Barbell Row",
        "muscle_group": "back",
        "equipment": "barbell",
        "difficulty": "intermediate",
    },
    {
        "name": "Dumbbell Curl",
        "muscle_group": "arms",
        "equipment": "dumbbells",
        "difficulty": "beginner",
    },
    {
        "name": "Tricep Dip",
        "muscle_group": "arms",
        "equipment": "bodyweight",
        "difficulty": "beginner",
    },
    {
        "name": "Overhead Press",
        "muscle_group": "shoulders",
        "equipment": "dumbbells",
        "difficulty": "beginner",
    },
    {
        "name": "Lateral Raise",
        "muscle_group": "shoulders",
        "equipment": "dumbbells",
        "difficulty": "beginner",
    },
    {
        "name": "Plank",
        "muscle_group": "core",
        "equipment": "bodyweight",
        "difficulty": "beginner",
    },
    {
        "name": "Dead Bug",
        "muscle_group": "core",
        "equipment": "bodyweight",
        "difficulty": "beginner",
    },
    {
        "name": "Burpee",
        "muscle_group": "full_body",
        "equipment": "bodyweight",
        "difficulty": "intermediate",
    },
    {
        "name": "Kettlebell Swing",
        "muscle_group": "full_body",
        "equipment": "kettlebell",
        "difficulty": "intermediate",
    },
]


@app.get("/exercises")
def get_exercises():
    """Return exercise recommendations filtered by query params.

    Query params:
      - muscle_group (optional): chest, back, legs, arms, shoulders, core, full_body
      - equipment (optional): e.g. dumbbells, bodyweight, barbell
      - difficulty (optional): beginner, intermediate, advanced
    """
    muscle_group = request.args.get("muscle_group")
    equipment = request.args.get("equipment")
    difficulty = request.args.get("difficulty")

    if muscle_group is not None:
        muscle_group = muscle_group.strip().lower()
        if muscle_group not in VALID_MUSCLE_GROUPS:
            return (
                jsonify(
                    {
                        "error": "invalid muscle_group",
                        "allowed": sorted(VALID_MUSCLE_GROUPS),
                    }
                ),
                400,
            )

    results = EXERCISES
    if muscle_group:
        results = [e for e in results if e["muscle_group"] == muscle_group]
    if equipment:
        equipment = equipment.strip().lower()
        results = [e for e in results if e["equipment"] == equipment]
    if difficulty:
        difficulty = difficulty.strip().lower()
        results = [e for e in results if e["difficulty"] == difficulty]

    return jsonify(
        {
            "filters": {
                "muscle_group": muscle_group,
                "equipment": equipment,
                "difficulty": difficulty,
            },
            "count": len(results),
            "exercises": results,
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "exercise-suggestion"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
