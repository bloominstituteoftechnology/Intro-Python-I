from item import Item

class Treasure(Item):
  def __init__(self, name, value):
    return super().__init__(name)
    self.value = value
    self.picked_up = False

  # TODO: fill in logic for this method
  def on_take(self): pass

  def on_drop(self): pass