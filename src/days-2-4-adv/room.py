# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
    def take_item(self, item_name):
        index = 0
        for item in self.items:
            if item.name.upper() == item_name.upper():
                taken = self.items.pop(index)
                return taken
            index += 1
        return None
    def __getitem__(self, key):
      return getattr(self, key)