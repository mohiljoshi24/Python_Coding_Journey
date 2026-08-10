from flask import Flask, jsonify
from storage_manager import load_data

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "classroom management system api is live"
    })

@app.route("/api/rooms", methods=["GET"])
def get_room():
    rooms = load_data("rooms.json")
    return jsonify({
        "status": "success",
        "count": len(rooms),
        "data": rooms
    }), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)