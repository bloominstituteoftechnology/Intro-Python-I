# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        current_items = ""
        for item in self.items:
            current_items = f'{current_items}' + \
                f' {item.name}: {item.description},'
        current_items = current_items[:-1]
        return f'\n\n{self.name}\n\n {self.description}\n\n You find the following items within...{current_items}'

    def print_room_description(self, player):
        if player.has_light():
            print(str(self))
        else:
            print("You cannot see anything.")

    def get_room_in_direction(self, direction):
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

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def find_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None
