"""Exercise Suggestion Microservice — Flask REST API starter."""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/exercises")
def get_exercises():
    """Return exercise recommendations as JSON.

    Example query params teammates can support later:
      ?type=cardio&level=beginner
    """
    # Placeholder response — replace with real recommendation logic.
    exercise_type = request.args.get("type", "any")
    level = request.args.get("level", "any")

    return jsonify(
        {
            "message": "Exercise Suggestion Microservice starter",
            "filters": {"type": exercise_type, "level": level},
            "exercises": [
                {
                    "name": "Brisk Walk",
                    "type": "cardio",
                    "level": "beginner",
                    "duration_minutes": 20,
                }
            ],
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "exercise-suggestion"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
