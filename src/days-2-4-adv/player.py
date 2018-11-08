from room import Room
from item import Item

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, player_items, score):
        self.name = name
        self.current_room = current_room
        self.player_items = player_items
        self.score = score

    def take_item(self, item_object):
        item_object.on_take(self)
        self.player_items.append(item_object)
        self.current_room.room_items.remove(item_object)

    def drop_item(self, item_object):
        item_object.on_drop()
        self.current_room.room_items.append(item_object)
        self.player_items.remove(item_object)