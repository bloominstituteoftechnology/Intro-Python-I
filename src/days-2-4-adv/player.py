# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, startRoom, items):
        self.startRoom = startRoom
        self.name = name
        self.items = items
    def enter(self, direction):
        room = self.currentRoom.getRoom(direction)
        if room is not None:
            self.currentRoom = room
            print (f"""
    {room.name}:
    {room.description}
    """)
        else:
            print (f"""
    Cannot go there
            """)
