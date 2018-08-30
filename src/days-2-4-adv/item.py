class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print("You have picked up the {}.".format(self.name))

    def on_drop(self, room):
        print("You have dropped the {} in the {}".format(
            self.name, room))


class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def on_take(self):
        print("You have picked up the {}.".format(self.name))


class LightSource(Item):
    def __init(self, name, description):
        super().__init__(name, description)
