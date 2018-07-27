# Write a class to hold player information, e.g. what room they are in
# currently.

from item import LightSource
class Player:
    def __init__(self, current_room, score = 0):
        self.current_room = current_room
        self.inventory = []
        self.score = score

    def handle_user_input(self, user_input):
        self.user_input = user_input
        if len(self.user_input.split()) == 1:
            self.handle_one_word_command()
        else:
            self.handle_two_word_command()

    def handle_one_word_command(self):
        if self.user_input == 'i' or self.user_input == 'inventory':
            self.list_inventory()
        elif self.user_input == 'score':
            self.display_score()
        else:
            self.move(self.user_input)

    def display_score(self):
        print(f'Current score is {self.score}')

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

    def light_source_exists(self):
        if self.current_room.is_light:
            return True
        if [ item for item in self.inventory if isinstance(item, LightSource) ]:
            return True
        if [ item for item in self.current_room.items if isinstance(item, LightSource) ]:
            return True

        return False

    def get(self, item_name):
        # get index of item we're getting
        index = next((i for i, item in enumerate(self.current_room.items) if item.name == item_name), -1)
        if index != -1:
            if not self.light_source_exists():
                print("Good luck finding that in the dark!")
                return

            gotten_item = self.current_room.items.pop(index);
            self.inventory.append(gotten_item)
            gotten_item.on_take(self)
        else:
            print(f'Error! {item_name} is not present in this room')

    def drop(self, item_name):
        # get index of item we're dropping
        index = next((i for i, item in enumerate(self.inventory) if item.name == item_name), -1)
        if index != -1:
            dropped_item = self.inventory.pop(index);
            self.current_room.items.append(dropped_item)
            dropped_item.on_drop()
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
