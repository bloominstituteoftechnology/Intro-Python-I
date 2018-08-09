# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self._registry = []
        for item in items:
            self._registry.append(item.name)

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                self._registry.remove(item.name)
                return item

    def add_item(self, item):
        self.items.append(item)
        self._registry.append(item.name)
        return




