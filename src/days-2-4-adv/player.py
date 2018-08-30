# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, startLocation, items):
        self.name = name
        self.location = startLocation
        self.items = items
    def change_location(self, new_location):
        self.location = new_location
    def add_item(self, item):
        self.items.append(item)
    def drop_item(self, item):
        for itim in self.items:
            if itim == item:
                self.items.remove(itim)
    def show_inventory(self, item):
        return "self.item"
    #def __repr__(self):
        #return "Current Location: {}".format(self.location)
    def __str__(self):
        return "Current Location: {}".format(self.location.title) 