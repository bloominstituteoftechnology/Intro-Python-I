# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, c_room):
        self.c_room = c_room

    def __update_room__(self, room):
        self.c_room = room
