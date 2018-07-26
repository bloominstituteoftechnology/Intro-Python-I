from lightsource import LightSource
import textwrap

class Room:
    def __init__(self, name, description, illuminated, items=[]):
        self.name = name
        self.description = description
        self.connections = {}
        self.illuminated = illuminated
        self.items = items

    def has_item(self, item_name):
        return item_name in [item.name for item in self.items]

    def get_item(self, item_name):
        return [item for item in self.items if item.name == item_name][0]

    def remove_item(self, item):
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)

    def is_illuminated(self):
        return self.illuminated or self.has_light_source()

    def has_light_source(self):
        len([item for item in self.items if isinstance(item, LightSource)]) > 0

    def describe(self):
        return textwrap.fill(self.description)

    def __str__(self):
        return self.name