# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, item):
        # starting attributes of the class
        self.name = name
        self.description = description
        self.item = None
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return f"\n\n{self.name}\n\n   {self.description}\n {self.item}\n"
        # upon entering each room, a string will print with the name of the room, it's decription
        # this is done with an f string, with white space to denote hierarchy when the statement is printed
    def getRoomInDirection(self, direction): #function to move player in inputed direction
        # if statement to match player input to movement direction: 'n' to north, 's' to south, etc.
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None