# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []
#THIS CREATES THE PLAYER CLASS THAT
#DEFINES THE ATTRIBUTES OF PLAYER