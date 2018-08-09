# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, room, items):
        self.room = room
        self.items = items
        self._registry = []
        for item in items:
            self._registry.append(item.name)

    def add_item(self, item):
        self.items.append(item)
        self._registry.append(item.name)
        return

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                self._registry.remove(item.name)
                return item