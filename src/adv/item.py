class Item():
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def on_drop(self):
    print("\nYou removed %s from your inventory." % (self.name))



class Treasure(Item):
  def __init__(self, name, description, value):
    super().__init__(name, description)
    self.value = value



class LightSource(Item):
  def __init__(self, name, description):
    super().__init__(name, description)

  def on_drop(self):
    print("\nYou removed %s from your inventory." % (self.name))
    print("\nIt's not wise to drop your source of light!\n")

  def on_use(self):
    print("\nYou turn on the %s and can finally see!\n" % self.name)