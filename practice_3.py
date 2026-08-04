import json

def load_room(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data

rooms_lists = load_room("rooms.json")

print("=== LOADED ROOMS FROM JSON ===")

for room in rooms_lists:
    print(f"room name: {room['room']} | capacity: {room['capacity']}")
