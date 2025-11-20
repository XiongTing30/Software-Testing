# app/checkout_service.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/checkout", methods=["POST"])
def checkout():
    data = request.get_json()
    items = data.get("items", [])

    if not items:
        return jsonify({"error": "empty cart"}), 400

    total = sum(item["price"] * item["quantity"] for item in items)
    return jsonify({"total": total, "status": "ok"}), 200
