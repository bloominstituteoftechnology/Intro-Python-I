# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, location, description, is_light):
        self.location = location
        self.description = description
        self.items = []
        self.is_light = is_light

    def __str__(self):
        return f'{self.location}: {self.description}'

    def add_room_item(self, item):
        self.items.append(item)

    def remove_room_item(self, item):
        self.items.remove(item)

    def list_room_items(self):
        if len(self.items) > 0:
            for i in self.items:
                print(i)
        else:
            print('You see nothing of interest in this room.')
