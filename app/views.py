from flask import jsonify
from app import app

@app.route("/")
@app.route("/index")
def index():
    return "Hello, World!"

@app.route("/result", methods=["GET"])
def getResult():
    return jsonify(
        {
            "washCar": False,
            "predictionBasis": {
                "daysUntilRain": 3,
                "precipitation": 0.6
            },
            "weatherDetails": {
                "one": "two"
            }
        }
    )