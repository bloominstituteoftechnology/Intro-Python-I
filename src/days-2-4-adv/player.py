# Write a class to hold player information, e.g. what room they are in
# currently.
class Player(object):
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom 
    def __repr__(self):
        return f"{self.name} currently in room {self.currentRoom}"
    def change_rooms(self, direction):
        direction = direction.lower()
        if self.currentRoom == 'outside':
            if direction == "n":
                pass
            else:
                return "You can not go in that direction!"
        elif self.currentRoom == 'foyer':
            if direction == "w":
                return "You can not go in that direction!"
        elif self.currentRoom == 'overlook':
            if direction == "s":
                return "You can not go in that direction!"
        elif self.currentRoom == 'narrow':
            if direction == "e":
                return "You can not go in that direction!"
        elif self.currentRoom == 'treasure':
            if direction == "s":
                pass
            else:
                return "You can not go in that direction!"