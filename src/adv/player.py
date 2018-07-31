# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def _init_(self, startRoom, name, health, items):
    self.currRoom = startRoom
    self.name = name
    self.inventory = []
    self.health = health
    def update_name(self, name):
      self.name = name
    def update_room(self, room):
      self.currRoom = room
    def take_item(self, inventory)
      
    