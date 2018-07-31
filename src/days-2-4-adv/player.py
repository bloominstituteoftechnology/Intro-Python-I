# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
  def __init__(self, name, currentRoom, health, items):
    self.currentRoom = currentRoom
    self. name = name
    self.health = health
    self.items = []
    def update_name(self, name):
      return self.name = name
    def update_room(self, room):
      return self.currentRoom = room
    def take_item(self, items, item):
      return self.items = self.items.append(item)
    def update_health(self, health):
      return self.health = int(health)
    def drop_item(self, currentRoom, items, item):
      return self.items.remove(item[0])