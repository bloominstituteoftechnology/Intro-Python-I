# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, abr, items):
        self.name = name
        self.description = description
        self.abr = abr
        self.items = items
        self.n_to = None
        self.w_to = None
        self.s_to = None
        self.e_to = None

    def room_items(self):
        if len(self.items) is not 0:
            print('\nThis room contains: ')
            for i, item in enumerate(self.items):
                print(str(i) + ' -> ' + item.name + ': ' + item.description)
        else:
            print('\nThere are no items in this room!')

    def delete_item(self, index):
        if len(self.items) is 0:
            print('\nThe room is totally empty!')
        else:
            del self.items[index]

    def dropped_item(self, item):
        self.items.append(item)