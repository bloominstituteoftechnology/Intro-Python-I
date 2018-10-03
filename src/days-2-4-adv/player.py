# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def travel(self, direction):
        nextRoom = self.current_room.getRoom(direction)
        if nextRoom is not None:
            self.current_room = nextRoom
            print(nextRoom)
        else:
            print('You are filled with an overwhelming sense of dread and quickly reconsider your decision.')