# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
    def travel(self, direction):
        new_room = self.room.get_rooms(direction)
        if new_room:
            self.room = new_room
    def look(self, direction):
        new_room = self.room.get_rooms(direction)
        if new_room:
            print(f'LOOKING into the {new_room.name}')
        else:
            print('Your nose in a brick wall man! Chose another direction to look at before you embarass yourself!')
    

        
        
