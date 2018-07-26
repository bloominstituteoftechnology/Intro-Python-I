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

    def take_item_from_room(self, item_name, room):
        item = room.take_item(item_name)
        item.on_take(self)
        self.items.append(item)

    def drop_item_in_room(self, item_name, room):
        item = self.get_item(item_name)
        self.items.remove(item)
        self.room.put_item(item)

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
