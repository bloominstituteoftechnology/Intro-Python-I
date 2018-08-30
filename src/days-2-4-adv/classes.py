class Room:
    def __init__(self, name, description, items=[], adjacent_rooms={}):
        self.name = name
        self.description = description
        self.items = items
        self.adjacent_rooms = adjacent_rooms
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        del self.items[self.items.index(item)]
    def check_for_item(self, item_name):
        return item_name in self.items

class Player:
    def __init__(self, room, items=[]):
        self.room = room
        self.items = items
    def get(self, item):
        self.items.append(item)
    def drop(self, item):
        del self.items[self.items.index(item)]
    def check_for_item(self, item_name):
        return item_name in self.items

class Item:
    def __init__(self, name):
        self.name = name
