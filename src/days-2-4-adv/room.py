# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = []

    def __str__(self):
        return f'\n {self.name} \n {self.desc} \n'

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)