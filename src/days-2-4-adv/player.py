# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom, items):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []
        if items is not None:
            self.items.append(items)

    invntry = "No items in inventory"

    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print("\n{}".format(nextRoom))
        else:
            print('\n You\'ve run into a brick wall! Try another direction')

    def look(self, direction=None):
        if direction is None:
            print(self.currentRoom)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                print("\n What you see: {}".format(nextRoom))

            else:
                print("There is nothing there.")

    def get(self, item):
        newItem = self.currentRoom.getItemFromRoom(item)
        if newItem is not None:
            self.items.append(newItem)
            print("\nNew Inventory: {}\n".format(', '.join([item.name for item in self.items])))
        else:
            print('\nThat item is not in this room.\n')

    def drop(self, item):
        if item in self.items:
            dropItem = self.currentRoom.dropItemInRoom(item)
            if dropItem is not None:
                self.items.remove(dropItem)
        else:
            print("\nYou do not currently have (a) {}. Type \'inventory\' to see a list of your items.\n".format(item.name))

    def inventory(self):
        if len(self.items) != 0:
            invntry = "\nInventory: {}\n".format(', '.join([item.name for item in self.items]))
        else:
            invntry = "No items in inventory"

        print(invntry)
