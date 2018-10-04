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
        if cmd == "pickup" and item not in self.items:
            if self.currentRoom.toggleItem(cmd, item) is not None:
                self.items.append(item)
                print (f"\npicked up this {item}\n")
            else:
                print ("\nthat isn't in this room\n")
        elif cmd == "drop" and item in self.items:
            if self.currentRoom.toggleItem(cmd, item) is not None:
                self.items.remove(item)
                print (f"\nwho needs this {item} anyway\n")
        else: 
            print ("\ncan't drop whatcha don't have\n")