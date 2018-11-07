from item import Item

class Treasure(Item):
  def __init__(self, name, value):
    return super().__init__(name)
    self.value = value
    self.picked_up = False