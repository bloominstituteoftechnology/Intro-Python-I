# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []
        self.score = 0
        self.light = False

    def enter(self, direction):
        room = self.currentRoom.getRoom(direction)
        if room is not None:
            self.currentRoom = room
            if room.light == True or self.light == True:
                print (f"\n{room.name}:\n\n{room.description}\n")
                room.getItem()
            else:
                print ("\nmy god, it's heckin dark, we need a light\n")
        else:
            print ("\nYo you cant go that way dog, duh, ya dingus\n")

    def itemHandler(self, cmd, item):
        if cmd == "take":
            hasItem = False
            for each in self.items:
                if each.name == item:
                    hasItem = True
            currentItem = self.currentRoom.toggleItem(cmd, item)
            if hasItem == False and currentItem is not None:
                self.items.append(currentItem)
                print (f"\npicked up this {currentItem.name}\n{currentItem.description}\n")
                if hasattr(currentItem, "onTake"):
                    self.score += currentItem.onTake()
                if hasattr(currentItem, "brightness"):
                    self.light = True
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
                    if hasattr(current, "onDrop"):
                        self.light = False
                else: 
                    print ("\ncan't drop whatcha don't have\n")