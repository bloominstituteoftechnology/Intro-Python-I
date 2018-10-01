# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, c_room):
        self.c_room = c_room
        self.items = []

    def update_room(self, room):
        self.c_room = room

    def get_item(self, item):
        self.items.append(item)

    def list_player_items(self):
        for i in self.items:
            print(i)
