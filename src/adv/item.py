class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

class Food(Item):
  def __init__(self, name, description, hungerValue):
    Item.__init__(self, name, description)
    self.hungerValue = hungerValue

class Weapon(Item):
  def __init__(self, name, description, damage):
    Item.__init__(self, name, description)
    self.damage = damage

class Armor(Item):
  def __init__(self, name, description, mitigation):
    Item.__init__(self, name, description)
    self.mitigation = mitigation

class Treasure(Item):
  def __init__(self, name, description, value, scored = False):
    Item.__init__(self, name, description)
    self.value = value
    self.scored = scored

class LightSource(Item):
  def __init__(self, name, description, light = False):
    Item.__init__(self, name, description)
    self.light = light