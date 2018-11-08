# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items_list=None, armor_list=None):
        self.name = name
        self.description = description
        self.items = items_list
        self.armor = armor_list

    def __str__(self):
        return f'{self.name}:\n{self.description}.'
