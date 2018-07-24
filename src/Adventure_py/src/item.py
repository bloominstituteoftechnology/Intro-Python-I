class Item(object):
    def __init__(self, name=None, description=None, value=0):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Weapon(Item):
    def __init__(self, name=None, dps=0, description=None, value=None):
        self.dps = dps
        super(Weapon, self).__init__(name, description, value)
