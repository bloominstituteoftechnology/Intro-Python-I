# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, room, inventory=[], equipments=[]):
        self.name = name
        self.location = room
        self.inventory = inventory
        self.equipments = equipments

    def getInventory(self):
        return ', '.join([i.name for i in self.inventory])

    def getEquipment(self):
        return ', '.join([i.name for i in self.equipments])