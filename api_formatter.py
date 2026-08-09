from storage_manager import load_data

def format_api_response(data, status_code=200):
    if status_code == 200:
        return {
            "status": "success",
            "code": status_code,
            "count": len(data),
            "data": data
    }

    else: 
        return {
            "status": "error",
            "code": status_code,
            "message": "failed to fetch data from storage"
    }

# load rooms from disk 
raw_rooms = load_data("rooms.json")

# formatted it into successfull api (http 200)
api_response = format_api_response(raw_rooms, status_code=200)

#simulated api response demo
print("=== simulated api response for frontend ===")
print(f"status: {api_response['status']}")
print(f"http code: {api_response['code']}")
print(f"total rooms returned: {api_response['count']}")
print(f"payload: {api_response['data']}")