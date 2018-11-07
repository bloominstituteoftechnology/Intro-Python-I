# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current):
        self.name = name
        self.current = current

    def move_to(self, direction):
        if direction:
            self.current = self.current.to_new(direction)
        else:
            print("You can't go that way.")
