# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def NextRoom(self, s_to, n_to, e_to, w_to):
        self.s_to = s_to
        self.n_to = n_to
        self.e_to = e_to
        self.w_to = w_to
