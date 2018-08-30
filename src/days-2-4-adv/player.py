# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, startLocation, equipment[], inventory[]):
        self.location = startLocation
        self.equipment = equipment
        self.inventory = inventory
    

    def change_location(self, new_location):
        self.location = new_location
    def __repr__(self):
        return "Current Location: {}".format(self.location)
    def __str__(self):
        return "Current Location: {}".format(self.location)
    def getInventory(self):
        return ', '.join([i.name for i in self.inventory])
    def getEquipment(self):
        return ', '.join([i.name for i in self.equipments])