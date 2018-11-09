# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, is_light):
        self.name = name
        self.description = description
        self.is_light = is_light
        self.item_list = []

    def __str__(self):
        return self.name
        
    def add_items(self, *items):
        for item in items:
            if type(item) == list:
                for i in item:
                    self.item_list.append(i)
            else:
                self.item_list.append(item)
    
    def remove_items(self, *items):
        for item in items:
            if type(item) == list:
                for i in item:
                    self.item_list.remove(i)
            else:
                self.item_list.remove(item)
