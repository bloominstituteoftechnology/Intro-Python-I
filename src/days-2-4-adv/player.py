# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []

    def enter(self, direction):
        room = self.currentRoom.getRoom(direction)
        if room is not None:
            self.currentRoom = room
            print (f"\n{room.name}:\n\n{room.description}\n")
        else:
            print ("\nYo you cant go that way dog, duh, ya dingus\n")

    def itemHandler(self, cmd, item):
        if cmd == "pickup" and len(self.items) == 0:
            currentItem = self.currentRoom.toggleItem(cmd, item)
            if currentItem is not None:
                self.items.append(currentItem)
                print (f"\npicked up this {currentItem.name}\n{currentItem.description}\n")
            else: 
                print ("\nthat isn't in this room\n")
        elif cmd == "pickup" and len(self.items) != 0:
            hasItem = False
            for each in self.items:
                if each.name == item:
                    hasItem = True
            currentItem = self.currentRoom.toggleItem(cmd, item)
            if hasItem == False and currentItem is not None:
                self.items.append(currentItem)
                print (f"\npicked up this {currentItem.name}\n{currentItem.description}\n")
            else:
                print ("\nthat isn't in this room\n")
        elif cmd == "drop":
            for each in self.items:
                if each.name == item:
                    global current
                    current = each
            if "current" not in globals():
                print ("\ncan't drop whatcha don't have\n")
            else:
                current2 = self.currentRoom.toggleItem(cmd, current)
                if current2 is not None:
                    self.items.remove(current)
                    print (f"\nwho needs this {current.name} anyway\n")
                else: 
                    print ("\ncan't drop whatcha don't have\n")