# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room


class Player(Room):

    def __init__(self, player_name, room_name="Outside Cave Entrance", room_description="North of you, the cave mount beckons", player_hp=100, player_attack=10):
        self.player_name = player_name
        super().__init__(room_name, room_description)
        self.player_hp = player_hp
        self.player_attack = player_attack

    def __str__(self):
        return "< PLAYER OBJECT player_name: %s, player_hp: %s, player_attack: %s, room_name: %s" \
               " room_description: %s >" % (self.player_name, self.player_hp, self.player_attack, self.room_name,
                                                   self.room_description)
