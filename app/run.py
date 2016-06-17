import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

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

if __name__ == "__main__":
    app.run(port=5000)