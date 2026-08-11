from flask import Flask, jsonify, request
from storage_manager import load_data, save_data

app = Flask(__name__)
DATA_FILE = "rooms.json"

@app.route("/api/rooms", methods=["GET"])
def get_rooms():
    rooms = load_data(DATA_FILE)
    return jsonify({
        "status": "success",
        "count": len(rooms),
        "data": rooms
    }), 200

@app.route("/api/rooms", methods=["POST"])
def add_room():
    # Step A: Capture incoming JSON data from client
    incoming_data = request.get_json()

    # Step B: Basic validation
    if not incoming_data or "id" not in incoming_data or "name" not in incoming_data:
        return jsonify({
            "status": "error",
            "message": "Invalid payload! 'id' and 'name' are required."
        }), 400

    # Step C: Read existing data, append new item, save to disk
    rooms = load_data(DATA_FILE)
    rooms.append(incoming_data)
    save_data(DATA_FILE, rooms)

    # Step D: Return success response
    return jsonify({
        "status": "success",
        "message": f"Room '{incoming_data['name']}' added successfully!",
        "data": incoming_data
    }), 201

# Add this block to start the server!
if __name__ == "__main__":
    app.run(debug=True, port=5000)