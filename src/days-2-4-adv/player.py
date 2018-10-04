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
        print(f'You have picked up the {item.name}. It is {item.description}')
    def selectItem(self, name):
        for item in self.inventory:
            if item.name.lower() == name.lower():
                return item
        return None
    def removeItem(self, item):
        if len(self.inventory) > 0:
            self.inventory.remove(item)
            self.startRoom.items.append(item)
            print(f'You dropped the {item.name}')
        else:
            print('No items to drop')
    def getInventory(self):
        print('You are carrying: \n')
        for item in self.inventory:
            print(f' {item.name} -- {item.description} ')

