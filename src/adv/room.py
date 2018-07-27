from lightsource import LightSource
import textwrap

class Room:
    def __init__(self, name, description, illuminated, items=[], monsters=[]):
        self.name = name
        self.description = description
        self.connections = {}
        self.illuminated = illuminated
        self.items = items
        self.monsters = monsters

    def monster_count(self):
        return len(self.monsters)

    def has_monster(self, monster_name):
        if monster_name == "it" and self.monster_count is 1:
            return True

        return monster_name in [monster.name for monster in self.monsters if monster.name == monster_name]

    def get_monster(self, monster_name):
        if monster_name == "it" and self.monster_count is 1:
            return self.monsters[0]

        return [monster for monster in self.monsters if monster.name == monster_name][0]

    def remove_monster(self, monster):
        self.monsters.remove(monster)

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