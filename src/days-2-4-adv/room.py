# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description 
        self.n_to = None # North to
        self.s_to = None # South to
        self.e_to = None # East to
        self.w_to = None # West to
    def __str__(self):
        return f'\n\n{self.name}\n    {self.description}\n'