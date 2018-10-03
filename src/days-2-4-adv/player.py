# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def travel(self, direction):
        next_room = self.current_room.getRoomInDirection(direction)
        if next_room is not None:
            self.current_room = next_room
            print(f'you have reached the... {next_room}')
        else:
            print("You took a wrong turn! Try another direction.")
