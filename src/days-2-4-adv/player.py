# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Light
from item import Treasure

class Player:
    def __init__(self, name, currentRoom, items):
        self.name = name
        self.currentRoom = currentRoom
        self.items = items
        self.score = 0


    def hasLight(self):
        for object in self.items:
            if isinstance(object, Light):
                print('You have a light')
                return True
            else:
                continue
        return False

    def isTreasure(self, item):
        if isinstance(item, Treasure):
            return True
        else:
            return False


    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            if nextRoom.hasLight() or self.hasLight():
                print("\n{}".format(nextRoom))
            else:
                print("\nYou've moved, but it's pitch black in here! Let's find some light.\n")
        else:
            print('\n You\'ve run into a brick wall! Try another direction')

    def look(self, direction=None):
        if direction is None:
            if self.hasLight() or self.currentRoom.hasLight():
                print(self.currentRoom)
            else:
                print("It's pitch black in here! Get a light.")
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                if self.hasLight() or nextRoom.hasLight():
                    print("\n  What you see: {}\n".format(nextRoom))
                else:
                    print("\nIt's pitch black in there! Get a light to see.\n")
            else:
                print("\nThere is nothing there.\n")

    def get(self, item):
        newItem = self.currentRoom.getItemFromRoom(item)
        if newItem is not None:
            self.items.append(newItem)
            newItem.on_take()
            if self.isTreasure(newItem):
                if newItem.value != 0:
                    self.score += newItem.value
                    print('Score: {}'.format(self.score))
        else:
            print('\nThat item is not in this room.\n')

    def drop(self, item):
        if item in self.items:
            dropItem = self.currentRoom.dropItemInRoom(item)
            if dropItem is not None:
                self.items.remove(dropItem)
                dropItem.on_drop()
        else:
            print("\nYou do not currently have (a) {}. Type \'inventory\' to see a list of your items.\n".format(item.name))

    def inventory(self):
        if len(self.items) != 0:
            invntry = "Inventory: {}\n".format(', '.join([item.name for item in self.items]))
        else:
            invntry = "No items in inventory"

        print(invntry)
