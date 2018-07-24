# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, room)
   self.room = room

  def playerLocation(self):
    return "You are at {}!".format(self.name)

  def playerMove(self):


playerCharacter = Player("outside")