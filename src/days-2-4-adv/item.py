class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return "{}".format(self.name)
    def on_drop(self):
        print("\nYou have dropped {}.\n".format(self.name))
    def on_take(self):
        print("\nYou have picked up {}.\n".format(self.name))


class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value
    def on_take(self):
        print("\nYou have picked up {}.\n".format(self.name))
        return self.value

class Light(Item):
    def __init__(self, name, description):
        Item.__init__(self, name, description)
    def on_drop(self):
        print("\nYou have dropped the {}.\n It's not wise to drop your light source...".format(self.name))
