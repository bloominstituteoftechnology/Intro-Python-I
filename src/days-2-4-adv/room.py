# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.searched = False

    def display_items(self):
        if len(self.items) > 0:
            for i in self.items:
                print('\t' + '* ' + i.name + '----' + i.description)
        else:
            print("**********Room has no items!**********")