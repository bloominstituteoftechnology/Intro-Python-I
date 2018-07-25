# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

item = {
    'tree':   Item("tree", "Just a tree"),
    'knife':  Item('knife', 'A very sharp knife'),
    'pig':    Item('pig', 'A wild boar'),
    'pen':    Item('pen', 'A foutain pen'),
    'gold':   Item('gold', '10 bars of gold'),
    'eggs':   Item('eggs', 'a dozen eggs'),
    'spoon':  Item('spoon', 'A golden spoon'),
}

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

    def handle_user_input(self, user_input):
        self.user_input = user_input
        if len(self.user_input.split()) == 1:
            self.handle_one_word_command()
        else:
            self.handle_two_word_command()

    def handle_one_word_command(self):
        if self.user_input == 'i' or self.user_input == 'inventory':
            self.list_inventory()
        else:
            self.move(self.user_input)

    def list_inventory(self):
        print(f'You have: {[i.name for i in self.inventory]}')

    def handle_two_word_command(self):
        commands = self.user_input.split()
        command = commands[0]
        item = commands[1]

        if command == 'get' or command == 'take':
            self.get(item)
        elif command == 'drop':
            self.drop(item)
        else:
            print("I don't understand that command\n")

    def get(self, item_name):
        if item_name in [i.name for i in self.current_room.items]:
            self.current_room.items = [i for i in self.current_room.items if i.name != item_name]
            self.inventory.append(item[item_name])
        else:
            print(f'Error! {item_name} is not present in this room')

    def drop(self, item_name):
        if item_name in [i.name for i in self.inventory]:
            self.inventory = [i for i in self.inventory if i.name != item_name]
            self.current_room.items.append(item[item_name])
        else:
            print(f'Error! You do not have {item_name} to drop')

    def move(self, direction):
        if hasattr(self.current_room, f'{direction}_to'):
            next_room = getattr(self.current_room, f'{direction}_to')
            if not next_room:
                print("You've reached a dead end!!!\n")
            else:
                self.current_room = next_room
        else:
            print("I don't understand that command\n")
