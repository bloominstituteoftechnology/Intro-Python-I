# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
from room import Room


class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.items = [None]

    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(nextRoom)
        else:
            print("You cannot move in that direction.")

    # def get(self, item):
    #     self.items.append(item['name'])


#    def look(self, direction=None):
#         if direction is None:
#             print(self.currentRoom)
#         else:
#             nextRoom = self.currentRoom.getRoomInDirection(direction)
#             if nextRoom is not None:
#                 print(nextRoom)
#             else:
#                 print("There is nothing there.")


# valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
#                     "forward": "n", "backwards": "s", "right": "e", "left": "w"}
