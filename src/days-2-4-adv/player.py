# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(nextRoom)
        else:
            print('\n You\'ve run into a brick wall! Try another direction')

    def look(self, direction=None):
        if direction is None:
            print(self.currentRoom)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                print(nextRoom)
            else:
                print("There is nothing there.")

    def get(self, item):
        newItem = self.currentRoom.getItemFromRoom(item)
        if newItem is not None:
            self.items.append(newItem)
        else:
            print('The specified item could not be found in this room :(')
