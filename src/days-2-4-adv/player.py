# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom, items, score):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []
        self.score = score
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print("\n-----------------------------------------------------")
            print(nextRoom)
            print("-----------------------------------------------------")
        else:
            print("You cannot move in that direction")
    def look(self, direction=None):
        if direction is None:
            print("\n-----------------------------------------------------")
            print(f"    You look around [{self.currentRoom.name}] and see:")
            if len(self.currentRoom.items) > 0:
                for item in self.currentRoom.items:
                    print(f"    {item.name}")
            else:
                print("    Nothing")
            print("-----------------------------------------------------")
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                print("-----------------------------------------------------")
                print(nextRoom)
                print("-----------------------------------------------------")
            else:
                print("-----------------------------------------------------")
                print("There is nothing there.")
                print("-----------------------------------------------------")
