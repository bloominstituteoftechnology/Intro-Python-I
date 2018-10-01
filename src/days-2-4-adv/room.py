# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, location, description, items=[]):
        self.location = location
        self.description = description
        self.items = items

    def __add_item__(self, item):
        self.items.append(item)
