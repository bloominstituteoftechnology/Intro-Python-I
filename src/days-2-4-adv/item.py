class Item:
    def __init__(self, name, description, equippable=None):
        self.name = name
        self.description = description
        self.equippable = False if equippable is None else True
        self.equipped = False

        def on_pickup(self):
            raise NotImplementedError

        def on_drop(self):
            raise NotImplementedError

# create a KEY subclass that can unlock doors when picked up

# create a LIGHTSOURCE subclass that can illuminate dark places