# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,name,descr):
     self.name = name
     self.descr = descr
     self.n_to = None
     self.e_to = None
     self.w_to = None
     self.s_to = None

    