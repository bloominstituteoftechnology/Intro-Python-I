# Implement a class to hold room information. This should have name and description attributes.

class Room:
  def __init__(self, name, description, is_light = True):
    self.name = name
    self.description = description
    self.is_light = is_light
    self.n_to = None
    self.s_to = None
    self.w_to = None
    self.e_to = None
    self.items = []


  def addItem(self, item):
    self.items.append(item)


  def removeItem(self, item):
    self.items.remove(item)
    return item


  def on_enter(self):
    if self.is_light is False:
      print("\nIt's pitch black in here!\n")
    
    print("Items in this room:")

    if len(self.items) is 0:
      print("   None")
    else:
      [print("   %s - %s" % (item.name, item.description)) for item in self.items]
      # map(lambda item: print("   %s - %s" % (item.name, item.description)), self.items)


  def itemAvailability(self, itemName):
    for item in self.items:
      if item.name.lower() == itemName.lower():
        return item
    return None