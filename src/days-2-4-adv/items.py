# Write a class for Items


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, p):
        p.addItem(self)

    def on_drop(self):
        pass

    def __str__(self):
        return self.name


class Treasure(Item):
    def __init__(self, name, description, value=10):
        super().__init__(name, description)
        self.value = value
        self.used = False

    def on_take(self, p):
        super().on_take(p)
        if not self.used:
            p.score += self.value
            self.used = True


class Weapon(Item):
    def __init__(self, name, description, damage=2, usage=10):
        super().__init__(name, description)
        self.damage = damage
        self.usageLeft = usage


class LightSource(Treasure):
    def __init__(self, name, description, fuel=10):
        super().__init__(name, description)
        self.fuel = fuel

    def on_drop(self):
        super().on_drop()
        print("YOU FOOL")

    def useFuel(self, player):

        for item in player.items:
            if self == item:
                self.fuel -= 1
                if self.fuel < 1:
                    player.dropItem(item)
                    print('you used up your light')

        
