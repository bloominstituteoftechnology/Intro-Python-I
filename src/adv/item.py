class Item:
  def __init__(self,name,description):
    self.name = name
    self.description = description

  def on_take(self):
    print("Player has picked up " + self.name)

  def on_drop(self):
    print("Player has dropped " + self.name)

class Treasure(Item):
  def __init__(self,name,description,value):
    super().__init__(name,description)
    self.value = value
  
class LightSource(Item):
  def __init__(self,name,description):
    super().__init__(name,description)
  
  def on_drop(self):
    print("It's not wise to drop your source of light!")

