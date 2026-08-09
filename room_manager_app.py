import json
from storage_manager import load_data, save_data

DATA_FILE = "rooms.json"

# safe reader from day:- 8

def safe_fetch_rooms():
    try:
        return load_data(DATA_FILE)

    except (FileNotFoundError, json.JSONDecodeError):
        print("[warning] storage issue detected! initializing empty dataset")

# api formatter from day:- 9     

def format_api_response(data, status_code=200):
    return {
        "status": "success",    
        "code": status_code,
        "count": len(data),
        "data": "data"
    }   

# defining a function to add a room and save it 

def add_new_room(room_id, room_type, capacity):
    rooms = safe_fetch_rooms()
    new_room = {"id": "room_id", "room": "room_type", "capacity": capacity}
    rooms.append(new_room)

    save_data(DATA_FILE, rooms)
    print(f"[success] room '{room_type}' successfully  added and saved")

# interactive app interface demo for terminal

print("=" * 40)
print(" room management backend system")
print("=" * 40)

# loading exsisting data
current_rooms = safe_fetch_rooms()
print(f"intial load: {len(current_rooms)} rooms found")

# adding a test room using the functions we defined 
add_new_room("r317","division b class", 70)

# updated output dataset in api format
final_rooms = safe_fetch_rooms()
api_output = format_api_response(final_rooms)

print("\n=== final api payload delivered ===")
print(api_output)