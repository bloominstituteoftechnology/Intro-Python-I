# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    move_error_msg = "You can not move that way! \n"

    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.score = 0
        self.items = []

    def move(self, direction):
        next_room = self.room.get_room_in_direction(direction)
        if next_room:
            self.room = next_room
            print(next_room)
            next_room.room_items()
        else:
            print('That is not a valid direction.')

    def look(self, direction):
        next_room = self.room.get_room_in_direction(direction)
        if next_room:
            print(next_room)
        else:
            print('There is nothing there')

    def get_item(self, item):
        if len(self.room.items) > 0:
            found_item = list(filter(lambda i: i.name.lower() == item, self.room.items))
            if len(found_item) > 0:
                self.items.append(found_item[0])
                self.room.remove_item(found_item[0])
                found_item[0].on_take(self)
            else:
                print('There is no such item, please try again.')

    def drop_item(self, item):
        if len(self.items) > 0:
            found_item = list(filter(lambda i: i.name.lower() == item, self.items))
            if len(found_item) > 0:
                self.items.remove(found_item[0])
                self.room.add_item(found_item[0])
            else:
                print('There is no such item, please try again.')

    def list_items(self):
        if self.has_items():
            print('Your inventory:')
            for i in self.items:
                print(i)
        else:
            print('Your inventory is empty.')

    def has_items(self):
        if len(self.items) > 0:
            return True
        return False
