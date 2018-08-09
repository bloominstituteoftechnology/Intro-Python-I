class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description        

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        self.picked_up = False

class LockedItem(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.unlocked = False
        self.unlock_item = unlock_item

        
