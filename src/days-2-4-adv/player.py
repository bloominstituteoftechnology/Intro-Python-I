# Write a class to hold player information, e.g. what room they are in
# currently.
class Player(object):
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom 
    def __repr__(self):
        return f"{self.name} currently in room {self.currentRoom}"
    def room_change (self, room):
        self.currentRoom = room
        return "Changing rooms..."