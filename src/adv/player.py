# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def move(self, direction):
        if direction == 'n':
            if not self.current_room.n_to:
                return True
            self.current_room = self.current_room.n_to
        elif direction == 'e':
            if not self.current_room.e_to:
                return True
            self.current_room = self.current_room.e_to
        elif direction == 's':
            if not self.current_room.s_to:
                return True
            self.current_room = self.current_room.s_to
        elif direction == 'w':
            if not self.current_room.w_to:
                return True
            self.current_room = self.current_room.w_to

        return False
