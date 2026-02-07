from flask import Flask, jsonify
from flask_cors import CORS
from ai_logic import compress_orders, predict_priority

app = Flask(__name__)
CORS(app)

orders = [
    {"item": "Burger", "type": "Veg", "quantity": 1, "prep_time": 5},
    {"item": "Burger", "type": "Veg", "quantity": 2, "prep_time": 5},
    {"item": "Pizza", "type": "Cheese", "quantity": 1, "prep_time": 8},
    {"item": "Fries", "type": "Regular", "quantity": 3, "prep_time": 3}
]

@app.route("/orders")
def get_orders():
    return jsonify({
        "compressed_orders": compress_orders(orders),
        "priority_orders": predict_priority(orders)
    })

if __name__ == "__main__":
    app.run(debug=True)
