from lightsource import LightSource

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []
        self.last_item = ''
        self.score = {
            'items': 0,
            'monsters': 0
        }

    def has_item(self, item_name):
        return item_name in [item.name for item in self.items]
    
    def get_item(self, item_name):
        return [item for item in self.items if item.name == item_name][0]

    def remove_item(self, item):
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)

    def take_item(self, item_name):
        item = self.room.get_item(item_name)
        if item.on_take(self):
            self.room.remove_item(item)
            self.add_item(item)

    def drop_item(self, item_name):
        item = self.get_item(item_name)
        if item.on_drop(self):
            self.remove_item(item)
            self.room.add_item(item)

    def can_see(self):
        return self.room.is_illuminated() or self.has_light_source()

    def has_light_source(self):
        return len([item for item in self.items if isinstance(item, LightSource)]) > 0

    def get_score(self):
        return sum(self.score.values())

    def add_score(self, category, amount):
        self.score[category] += amount

    def __str__(self):
        return self.name
