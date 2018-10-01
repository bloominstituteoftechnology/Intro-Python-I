# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, c_room, items=[]):
        self.c_room = c_room
        self.items = items

    def __update_room__(self, room):
        self.c_room = room

    def __get_item__(self, item):
        self.items.append(item)

    def __list_items__(self):
        for i in self.items:
            print(i)
