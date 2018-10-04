# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, startRoom):
        self.startRoom = startRoom
        self.name = name
        self.inventory = []

    def enter(self, direction):
        room = self.startRoom.getRoom(direction)
        if room is not None:
            self.startRoom = room
            print (f"""
    {room.name}:
    {room.description}
    """)
        else:
            print (f"""
    Cannot go there
            """)
    def addItem(self, item):
        self.inventory.append(item)
        self.startRoom.removeItem(item)
        print(f'You have picked up the {item.name}.')

