

class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  def getDescription(self):
    return self.description
  def __repr__(self):
    return f'{self.name} > -- {self.description}\n'
  def __str__(self):
    return f'{self.name} > -- {self.description}\n'


class Food(Item):
  def __init__(self, name, description, calories):
    Item.__init__(self, name, description)
    self.calories = calories
  def getDescription(self):
    return f'this is ' + self.description + f'. the calorie count is {self.calories}'  
  def __repr__(self):
    return f'{self.name} > -- {self.description}, {self.calories}\n'
  def __str__(self):
    return f'{self.name} > -- {self.description}, {self.calories}\n'