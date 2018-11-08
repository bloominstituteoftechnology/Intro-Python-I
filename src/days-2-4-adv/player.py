# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, room):
    self.name = name
    self.room = room 
    self.inventory = []

  def try_move(self, direction):
    key = direction + '_to'

    if not hasattr(self.room, key):
      print("No path lies in this direction. Pick another") 
      return self.room     
    else:
      return getattr(self.room, key)

  # --> For 'take', and 'get' --> Find the item given in rooms.item array
  def find_item(self, item_name): 
    print(self.room.items)   
    for item in self.room.items:
      print(item.name)
      if item.name.lower() == item_name:  
        return item
      else:
        print("in find_item")
        return None
    
  def find_in_inventory(self, item_name):
    for item in self.inventory:
      if item.name.lower() == item_name:
        return item
      else:
        print("nothing in find_in_inventory")
        return None
        
