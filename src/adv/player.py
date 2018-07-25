# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def move(self, direction):
        if hasattr(self.current_room, f'{direction}_to'):
            next_room = getattr(self.current_room, f'{direction}_to')
            if not next_room:
                print("You've reached a dead end!!!\n")
            else:
                self.current_room = next_room
        else:
            print("I don't understand that command\n")
