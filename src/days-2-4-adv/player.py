# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room, starting_items=[], starting_score=0):
        self.name = name
        self.current_room = current_room
        self.items = starting_items
        self.strength = 10
        self.score = starting_score

    def travel(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(f'you have reached the... {next_room}')
        else:
            print("You took a wrong turn! Try another direction.")

    def print_status(self):
        print(f"Your name is {self.name}, your strength is {self.strength}")

    def print_inventory(self):
        print("Your backpack contains...")
        for item in self.items:
            print(f" {item.name}: {item.description} \n")

    def print_score(self):
        print(f"Hey there {self.name}, your current score is {self.score}")

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def find_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

    def has_light(self):
        return True

    def drop_item(self, item_name):
        item_to_drop = self.find_item("".join(item_name))
        if item_to_drop is not None:
            self.remove_item(item_to_drop)
            self.current_room.add_item(item_to_drop)
            item_to_drop.on_drop()
        else:
            print("You do not currently possess that item")
