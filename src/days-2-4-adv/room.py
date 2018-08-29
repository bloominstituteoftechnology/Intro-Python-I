# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def getRmInDir(self, direction):
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

        '''  def connectRooms(self, destRoom, direction):
        if direction == 'n':
            self.n_to = destRoom
            destRoom.s_to == 's'
        elif direction == 's':
            self.s_to = destRoom
            destRoom.n_to == 'n'
        elif direction == 'e':
            self.e_to = destRoom
            destRoom.w_to == 'w'
        elif direction == 'w':
            self.w_to = destRoom
            destRoom.e_to == 'e'
        '''