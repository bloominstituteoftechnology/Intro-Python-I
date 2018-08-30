class Item:
  def __init__(self, name, description, value = 0):
    self.name = name
    self.description = description
    self.value = value
  def __repr__(self):
    return f'{self.name}'
  def __str__(self):
    return f'{self.name}'
  def getDescription(self):
    return self.description
  def on_drop(self):
    print(f'You have dropped {self.name}')

class Commodity(Item):
  def __init__(self, name, description, value):
      super().__init__(name, description, value)
      self.picked_up = False
      
  def on_take(self, player):
    if self.picked_up is False:
      player.score += self.value
      print(f'You get {self.value} points!')
      self.picked_up = True
    else:
      pass