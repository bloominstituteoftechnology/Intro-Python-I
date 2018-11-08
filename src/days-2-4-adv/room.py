# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc, is_lit=False):
        self.name = name
        self.desc = desc
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
        self.is_lit = is_lit

    def to_new(self, direction):
        if direction == "n" and self.n_to:
            return self.n_to
        if direction == "e" and self.e_to:
            return self.e_to
        if direction == "s" and self.s_to:
            return self.s_to
        if direction == "w" and self.w_to:
            return self.w_to
        else:
            print("You can't go that way.")

    def populate_item(self, item):
        self.items.append(item)

    def show_items(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\n===You find: ")
        for item in self.items:
            print(f"{item.name} - {item.desc}")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def remove_item(self, item):
        self.items.remove(item)

