class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player):
        print("You picked up %s." % self.description)

    def on_drop(self, player):
        print("You dropped a %s." % self.name)


class Treasure(Item):
    def __init__(self, name, description, value=1, taken=False):
        self.name = name
        self.description = description
        self.value = value
        self.taken = taken

    def on_take(self, player):
        print("You picked up %s." % self.description)
        if self.taken == False:
            player.score += self.value
            self.taken = True
            print("Looting treasure increases your score by %s!" % self.value)


class LightSource(Item):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_drop(self, player):
        print("It's not wise to drop your source if light!")
        print("You dropped a %s." % self.name)
