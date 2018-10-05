
class Items:
  def __init__(self, name, condition):
    self.items = []
    self.name = name
    self.condition = condition


class Weapon(Items):
  def __init__(self, name, condition, strength):
    Items.__init__(self, name, condition)
    self.name = name
    self.condition = condition
    self.strength = strength


class Asset(Items):
  def __init__(self, name, condition, value):
    Items.__init__(self, name, condition)
    self.name = name
    self.condition = condition
    self.value = value


class Tool(Items):
  def __init__(self, name, condition, use):
    Items.__init__(self, name, condition)
    self.name = name
    self.condition = condition
    self.use = use


class Food(Items):
  def __init__(self, name, condition, nutrition):
    Items.__init__(self, name, condition)
    self.name = name
    self.condition = condition
    self.nutrition = nutrition
