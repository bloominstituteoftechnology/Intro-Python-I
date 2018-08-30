# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def check_room(self):
        if len(self.items) == 0:
            print('Room is empty')
        else:
            for c, value in enumerate(self.items, 1):
                print('Room has: ' + value)
                # print('Room has: ' + str(c) + ' ' + value)
    def remove_item(self, item):
        for item in self.items:
            self.items.remove(item)
        
