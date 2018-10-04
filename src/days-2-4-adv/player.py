# Write a class to hold player information, e.g. what room they are in
# currently.
from item import LightSource

class Player:
    def __init__(self, name, currentRoom, items, score):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []
        self.score = score
    def hasLight(self):
        for item in self.items:
            if isinstance(item, LightSource):
                return True
                break
            else: return False
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            if self.currentRoom.is_light or self.hasLight():
                print("\n-----------------------------------------------------")
                print(nextRoom)
                print("-----------------------------------------------------")
            else:
                print("\n-----------------------------------------------------")
                print(f"\n    [{self.currentRoom.name}]\n\n    It's pitch black!\n")
                print("-----------------------------------------------------")
        else:
            print("You cannot move in that direction")
    def look(self, direction=None):
        if direction is None:
            if self.currentRoom.is_light or self.hasLight():
                print("\n-----------------------------------------------------")
                print(f"    You look around [{self.currentRoom.name}] and see:")
                if len(self.currentRoom.items) > 0:
                    for item in self.currentRoom.items:
                        print(f"    {item.name}")
                else:
                    print("    Nothing")
                print("-----------------------------------------------------")
            else:
                print("\n-----------------------------------------------------")
                print(f"\n    You look around the [{self.currentRoom.name}] and see:")
                print("\n    Nothing but complete darkness...")
                print("\n-----------------------------------------------------")

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
