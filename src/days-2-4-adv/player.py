# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    def travel(self, direction):
        nextRoom = self.current_room.getRoom(direction)
        if nextRoom is not None:
            self.current_room = nextRoom
            print(nextRoom)
        else:
            print('You are filled with an overwhelming sense of dread and quickly reconsider your decision.')
    def addItem(self, item):
        self.inventory.append(item)
        self.current_room.removeItem(item)
        print(f'You have picked up the {item.name}. It is {item.description}')
    def selectItem(self, name):
        for item in self.inventory:
            if item.name.lower() == name.lower():
                return item
        return None
    def removeItem(self, item):
        if len(self.inventory) > 0:
            self.inventory.remove(item)
            self.current_room.items.append(item)
            print(f'You dropped the {item.name}')
        else:
            print('No items to drop')
    def getInventory(self):
        print('You are carrying: \n')
        for item in self.inventory:
            print(f' {item.name} -- {item.description} ')