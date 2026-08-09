class room:
    def __init__(self, room_id, name, capacity):
        self.room_id = room_id
        self.name = name
        self.capacity = capacity

    def to_dict(self):
        return {
            "id": self.room_id,
            "name": self.name,
            "capacity": self.capacity
        }

    def is_suitable_for(self, group_size):
        return self.capacity >= group_size

# testing the model
lab = room("l201", "cloud computing lab", 45)

print(f"room name: {lab.name}")
print(f"can hold 50 people? {lab.is_suitable_for(50)}")
print(f"can hold 30 people? {lab.is_suitable_for(30)}")

print(f"dictionary format json: {lab.to_dict()}")
    

    
    
