# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self,name,descr,items):
     self.name = name
     self.descr = descr
     self.items = []

    def __str__(self):
        return f'{self.name}:\n{self.descr}:\n{self.items}.'

    def add_item(self, *args):
        self.items.extend(args)

    def remove_item(self, item):
        self.items.remove(item)