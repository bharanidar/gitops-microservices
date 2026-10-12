import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

USERS_URL = os.getenv(
    "USERS_URL", "http://localhost:5001"
)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/orders")
def orders():
    response = requests.get(
        f"{USERS_URL}/users", timeout=3
    )
    response.raise_for_status()
    users = response.json()

    return jsonify([
        {
            "order_id": 101,
            "user": users[0]["name"],
            "item": "Laptop"
        }
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
