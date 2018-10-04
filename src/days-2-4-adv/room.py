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
    def __str__(self):
        return f"\n\n{self.name}\n\n   {self.description}\n"
    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def room_items(self):
        if len(self.items) > 0:
            print('This room contains: ')
            for item in self.items:
                print(item.name, '--', item.description)
        else:
            print('There is nothing else in here.')

    def dropped_item(self, item):
        self.items.append(item)

    def delete_item(self, index):
        del self.items[index]