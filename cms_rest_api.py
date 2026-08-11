from flask import Flask, jsonify, request
from storage_manager import load_data, save_data

app = Flask(__name__)
DATA_FILE ="rooms.json"

def make_response(data=None, message=None, status_code=200):
    payload = {
        "status": "success" if status_code < 400 else "error",
        "status_code": status_code
    }
    if message:
        payload["message"] = message

    if data is not None:
        payload["data"] = data
        if isinstance(data, list):
            payload["count"] = len(data)

    return jsonify(payload), status_code

@app.route("/api/rooms", methods=["GET"])
def get_all_rooms():
    rooms = load_data(DATA_FILE)
    return make_response(data=rooms)

@app.route("/api/rooms/<room_id>", methods=["GET"])
def get_room_by_id(room_id):
    rooms = load_data(DATA_FILE)

    room = next((r for r in rooms if r.get("id") == room_id), None)

    if not room:
        return make_response(message=f"room '{room_id}' not found", status_code=404)

    return make_response(data=room)

@app.route("/api/rooms", methods=["POST"])
def create_room():
    payload = request.get_json()

    if not payload or "id" not in payload or "name" not in payload:
        return make_response(message="missing 'id' or 'name'", status_code=400)

    rooms = load_data(DATA_FILE)

    if any(r.get("id") == payload["id"] for r in rooms):
        return make_response(message=f"room id '{payload['id']}' already exsists", status_code=400)

    rooms.append(payload)
    save_data(DATA_FILE, rooms)

    return make_response(data=payload, message="room created successfully!", status_code=201)

if __name__ == "__main__":
    app.run(debug=True, port=5000)


