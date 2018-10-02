# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, c_room):
        self.c_room = c_room
        self.items = []
        self.score = 0

    def update_room(self, room):
        self.c_room = room

    def get_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.c_room.add_room_item(item)
        self.items.remove(item)

    def add_score(self, score):
        self.score += score

    def get_score(self):
        return self.score

    def list_player_items(self):
        return self.items

    def player_has_items(self):
        if len(self.items) > 0:
            return True
        else:
            return False
