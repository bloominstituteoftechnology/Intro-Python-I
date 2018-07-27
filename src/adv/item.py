class Item:
  def __init__(self, name, descript):
    self.name = name
    self.descript = descript
    self.points = 10
    self.posessed = False

  def on_take(self):
    self.posessed = True
    print("You picked up:", self.name)

  def on_drop(self):
    print('You dropped:', self.name)


class Treasure(Item):
  def __init__(self, name, descript, points):
    super().__init__(name, descript)
    self.points = points
    self.posessed = False

class LightSource(Item):
  def __init__(self, name, descript):
    super().__init__(name, descript)
    self.points = 15
    self.possessed = False
    self.is_source = True