from item import Item

class Treasure(Item):
  def __init__(self, name, value):
    return super().__init__(name)
    self.value = value
    self.picked_up = False

  # on_take method set picked_up to true
  def on_take(self):
    self.picked_up = True

  def on_drop(self): pass