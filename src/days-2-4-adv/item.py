class Item:
    def __init__(self, name, equippable=None):
        self.name = name
        self.equippable = False if equippable is None else True
        self.equipped = False

        def on_pickup(self):
            raise NotImplementedError

        def on_drop(self):
            raise NotImplementedError