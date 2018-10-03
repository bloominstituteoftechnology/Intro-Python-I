# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
#THIS MAKES THE ROOM CLASS THAT DEFINES THE ATTRIBUTES OF A ROOM        
    def __str__(self):
        return f"\n\{self.name}\n\n    {self.description}\n"
#THIS CREATES A STRING THAT PRINTS IN EACH ROOM