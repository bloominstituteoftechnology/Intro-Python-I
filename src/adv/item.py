
class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  
  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name


class Consumable(Item):
  def __init__(self, name, description, quantity, kind):
    super.__init__(name, description)
    self.quantity = quantity
    self.kind = kind
  
  def expend(self):
    pass
  

class Equippable(Item):
  def __init__(self, name, description):
    super.__init__(name, description)
    self.equipable = True
  

class Armor(Equippable):
  def __init__(self, name, description, protection):
    super.__init__(name, description)
    self.protection = protection
    self.slot = 'armor'
  

class Weapon(Equippable):
  def __init__(self, name, description, power):
    super.__init__(name, description)
    self.power = power
    self.slot = 'weapon'


class Accessory(Equippable):
  def __init__(self, name, description, effect):
    super.__init__(name, description)
    self.effect = effect
    self.slot = 'accessory'


class MagicItem(Equippable):
  def __init__(self, name, description, effect):
    super.__init__(name, description)
    self.effect = effect
    self.slot = 'magic item'


# Create all the items
item = {
  'lever': Item('lever', """It looks as though it was broken off at the base.
Maybe it goes to something."""),
}