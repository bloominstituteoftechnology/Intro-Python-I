# Item
# methods: use, 
class Item:
   def __init__(self, name, description, weight = 1):
      self.name = name
      self.description = description
      self.weight = 1
      self.firstPickup = True
   
   def itemInfo(self):
      print(f"a {self.name}")

class Treasure(Item):
   def __init__(self, name, description, value = 100):
      Item.__init__(self, name, description)
      self.value = value

   def onTake(self, player):
      if self.firstPickup : player.score += self.value
   
   def onDrop(self):
      pass