from room import Room, room
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.currentRoom = room['outside']
        self.badMove = '==You abruptly realize it is impossible to continue in this direction, turn around, and stride confidently back from whence you came.=='
    def __str__(self):
        return f'\n{self.name}\n Health: {self.health} - Mana: {self.mana} - Room: {self.currentRoom.name}'
    def playerMove(self, direction):
        if direction == 'n':
            self.currentRoom = self.currentRoom.n_to
        elif direction == 's': 
            self.currentRoom = self.currentRoom.s_to
        elif direction == 'e': 
            self.currentRoom = self.currentRoom.e_to
        elif direction == 'w': 
            self.currentRoom = self.currentRoom.w_to




# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


