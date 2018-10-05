# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, location, description, is_light):
        self.location = location
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        self.is_light = is_light
    def __str__(self):
        if len(self.items) > 0:
            return f'\n You have entered the {self.location} \n {self.description} \n As you look around you notice  {self.items[0].name} in the {self.location} '
        else:
            return f'\n You have entered the {self.location} \n {self.description} \n '
    def getRoom(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to
        else:
            return None
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        if len(self.items) > 0:
            self.items.remove(item)
        else:
            print('No items to drop')
        
    def selectItem(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None