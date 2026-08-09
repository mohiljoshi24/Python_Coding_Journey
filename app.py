from storage_manager import load_data, save_data

rooms = load_data("rooms.json")

new_room = {"id": "r301", "room": "auditorium 301", "capacity": 100}
rooms.append(new_room)

save_data("rooms.json", rooms)