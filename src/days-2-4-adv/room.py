# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
   def __init__(self,name, description, inventory = None, isLit = True):
      self.name = name
      self.description = description
      self.isLit = isLit
      if inventory != None: self.inventory = inventory
      else: self.inventory = {}

   def peekDirection(self, direction):
      try:
         if direction == 'n': return self.n_to
         elif direction == 's': return self.s_to
         elif direction == 'w': return self.w_to
         elif direction == 'e': return self.e_to
         else: return None
      except AttributeError:
        print('There is nothing in that direction')
        return None
   
   def roomInfo(self):
      print(self.name)
      print(self.description)
      self.roomContents()
      print("")

   def roomContents(self):
      numItems = len(self.inventory)
      if numItems > 0:
         endString = ""
         if numItems > 1: endString = "s"
         print(f"Around the room you see {numItems} item{endString}: ")
         for value in self.inventory.values():
            value.itemInfo()
      else: 
         print("This room is otherwise empty")
         print("")
