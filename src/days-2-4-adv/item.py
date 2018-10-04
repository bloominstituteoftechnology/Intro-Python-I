
class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def on_drop(self):
        print(f"You have dropped {self.name}.")

    def on_take(self):
        print(f"You have taken {self.name}.")


class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value

    def on_drop(self):
        print(f"You have dropped the {self.name}.")

    def on_take(self):
        return self.value


class LightSource(Item):
    def __init__(self, name, description):
        Item.__init__(self, name, description)

    def on_drop(self):
        print(f"You have dropped the {self.name}. It is not wise to drop your source of light!")
