# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
    
    def move_to(self, direction):
        if direction == 'n':
            self.room = self.room.to_room(direction)
        else:
            print("You can't go that way.")