class Item:
    def __init__(self, name, description, dmg):
        self.name = name
        self.description = description
        self.dmg = dmg
    def on_take(self, player, room):
        if room.is_light:
            player.inventory.append(self)
            room.inventory.remove(self)
            print("You have taken the %s." % self.name)
        else:
            print("Good luck finding that in the dark!\n")
    def on_drop(self, player, room):
        if not isinstance(self, Lightsource):
            player.inventory.remove(self)
            room.inventory.append(self)
            print("You have dropped the %s." % self.name)
        else:
            reallyDrop = input("It's not wise to drop your source of light! Do you really want to do so? Y/N ")
            if reallyDrop.upper() == "Y":
                player.inventory.remove(self)
                room.inventory.append(self)
                print("You have dropped the %s." % self.name)

class Treasure(Item):
    def __init__(self, name, description, value, dmg):
        super().__init__(name, description, dmg)
        self.value = value
        self.takenAlready = False
    def on_take(self, player, room):
        if room.is_light:
            self.takenAlready = True
            player.inventory.append(self)
            room.inventory.remove(self)
            print("You have taken the %s." % self.name)
        else:
            print("Good luck finding that in the dark!\n")

class Lightsource(Item):
    def __init__ (self, name, description, dmg):
        super().__init__(name, description, dmg)

class Food(Item):
    def __init__ (self, name, description, dmg, healValue):
        super().__init__(name, description, dmg)
        self.healValue = healValue