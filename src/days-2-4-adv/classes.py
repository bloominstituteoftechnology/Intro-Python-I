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
        for item in self.items:
            if item.name == item_name:
                return True
        return False

    def inventory(self):
        print(f"\nInside the room, you see the following items: {', '.join(item.name for item in self.items)}")

class Player:
    def __init__(self, room, items=[]):
        self.room = room
        self.items = items
        self.score = 0

    def get(self, item):
        self.items.append(item)

    def drop(self, item):
        del self.items[self.items.index(item)]

    def check_for_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return True
        return False

    def score_report(self):
        print(f"\nYour score is: {self.score}")

    def inventory(self):
        print(f"\nYou have the following items: {', '.join(item.name for item in self.items)}")

class Item:
    def __init__(self, name):
        self.name = name

class Treasure:
    def __init__(self, name, value):
        Item.__init__(self, name)
        self.value = value
        self.picked_up = False

    def on_take(self):
        self.picked_up = True
