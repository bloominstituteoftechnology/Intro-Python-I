# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        return f'\n{self.name}\n\n    {self.desc}\n\n'

    def get_room_in_direction(self, direction):
        if direction == 'n':
            if self.n_to:
                return self.n_to
        elif direction == 's':
            if self.s_to:
                return self.s_to
        elif direction == 'e':
            if self.e_to:
                return self.e_to
        elif direction == 'w':
            if self.w_to:
                return self.w_to
        else:
            return None

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def room_items(self):
        if len(self.items) > 0:
            print('Items:')
            for i in self.items:
                print(i)
        else:
            print('No items in this room.')

