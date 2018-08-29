# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, start_room):
        self.name = name
        self.current_room = start_room

    def __str__(self):
        return (self.name, self.current_room)
