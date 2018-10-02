# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room):
        self.room = room
        self.items = []

    def move(self, room):
        self.room = room

    def get_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)