# Write a class to hold player information, e.g. what room they are in
# currently.
class playerInfo:
   def __init__(self, room):
        self.room = room

    def position(self):
        return self.room