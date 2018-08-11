class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)      

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

class LockedItem(Item):
    # unlock_item is item that will unlock LockedItem
    def __init__(self, name, description, unlock_item):
        super().__init__(name, description)
        self.unlocked = False
        self.unlock_item = unlock_item




