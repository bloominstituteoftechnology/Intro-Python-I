# Write a class to hold player information, e.g. what room they are in
# currently.
from adv import room


class Player:
    def __init__(self):
        self.current_room = room["outside"]
        self.armor = []
        self.items = []

    def enter(self, current_room):
        self.current_room = current_room

    def pick_up(self, item):
        if item.type == "armor":
            self.armor.append(item)
        elif item.type == "weapon":
            self.items.append(item)

    def drop_item(self, item):
        if item.type == "armor":
            self.armor.remove(item)
        elif item.type == "weapon":
            self.items.remove(item)
