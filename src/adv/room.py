# Implement a class to hold room information. This should have name and
# description attributes.
from player import Player
from item import Item
from item import LightSource


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return "You are currently " + self.name + '.\n' + self.description

    def pickup(self, player, item):
        try:
            self.items.remove(item)
            player.addItem(item)
            item.onTake(player)
            return "Picked up " + item.name + "."
        except:
            return "There is no " + item.name + " around."

    def drop(self, player, item):
        if isinstance(self, DarkRoom) and isinstance(item, LightSource):
            print("It's not wise to drop your source of light!")
        try:
            player.removeItem(item)
            self.items.append(item)
            return "Dropped " + item.name + "."
        except:
            return "You're not carrying " + item.name + "."

    def viewItems(self):
        return self.items


class DarkRoom(Room):
    def __init__(self, name, description):
        super().__init__(name, description)

    def hasLightSource(self):
        for item in self.items:
            if isinstance(item, LightSource):
                return True
        return False
