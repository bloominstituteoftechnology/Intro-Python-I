# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    move_error_msg = "You can not go that way! \n"

    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.score = 0
        self.items = []

