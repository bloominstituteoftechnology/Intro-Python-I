# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room):
      self.room = room
    def setRoom(self, room):
      self.room = room
    def __getitem__(self, key):
      return getattr(self, key)
