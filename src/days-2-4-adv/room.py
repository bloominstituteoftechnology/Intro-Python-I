# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.item_list = []

    def add_items(self, *items):
        for item in items:
            if type(item) == list:
                for i in item:
                    self.item_list.append(i)
            else:
                self.item_list.append(item)
