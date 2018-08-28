# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(Room):
    def __init__(self, name, curRoom):
        super().__init__(curRoom)
        self.name = name