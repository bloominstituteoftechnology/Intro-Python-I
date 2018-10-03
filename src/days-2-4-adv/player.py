# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    move_error_msg = "You can not move that way! \n"

    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def move(self, direction):
        next_room = self.room.get_room_in_direction(direction)
        if next_room:
            self.room = next_room
            print(next_room)
        else:
            print('That is not a valid direction.')

    def look(self, direction):
        next_room = self.room.get_room_in_direction(direction)
        if next_room:
            print(next_room)
        else:
            print('There is nothing there')

    def get_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)
