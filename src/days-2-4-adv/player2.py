# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room


class Player(Room):

    def __init__(self, player_name):
        super().__init__()
        self.player_name = player_name
        self.player_items = []

    def __str__(self):
        return "< PLAYER OBJECT player_name: %s, room_name: %s, room_description: %s" \
               " room_items: %s >" % (self.player_name, self.room_name, self.room_description, self.items_list)

    def pick_up_items_in_room(self):
        print(self.player_items)
        print(self.get_items())
        return self.player_items + self.items_list
