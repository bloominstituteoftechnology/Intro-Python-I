# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items = None):
        self.name = name
        self.description = description
        self.items = items
    # def __str__(self):
    #     return('room: {}, {}, {}'.format(self.name, self.description, self.items.name))
    def take(self, item):
        self.items.append(item)
    def drop(self, item):
        self.items.remove(item)



