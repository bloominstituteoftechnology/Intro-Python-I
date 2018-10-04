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
        return self.name

    def next_room(self, direction):
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

    def print_items(self):
        for item in self.items:
            print(f"You find a {item.name.lower()} in this room!")

    def find_item(self, input_item):
        for item in self.items:
            if item.name.lower() == input_item.lower():
                return item
            return None

    def remove_item(self, item):
        print(f"You have picked up the {item.name.lower()}")
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)
        print(f"You have dropped the {item.name.lower()}")

class Dark_Room(Room):
    def __init__(self, name, description, items, visibility):
        super().__init__(name, description, items)
        self.visibility = visibility

    def light_on(self):
        self.visibility = True
