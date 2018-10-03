# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return f"\n{self.room}\n"


