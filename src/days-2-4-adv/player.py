# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        
    def getRoom(self):
        print(75 * '#')
        print('You are in: ' + self.room.name)
        print('Directions: ' + self.room.description)