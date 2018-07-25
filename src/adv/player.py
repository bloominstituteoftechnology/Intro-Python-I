# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'{self.current_room.description} \n north = {self.current_room.n_to} south = {self.current_room.s_to} east = {self.current_room.e_to} west = {self.current_room.w_to}'
    def change_room(self, newroom):
        self.current_room = newroom
        
