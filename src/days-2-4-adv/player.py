# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room, item_list = [], score = 0):
        self.room = room
        self.item_list = item_list
        self.score = score

    def add_items(self, *items):
        for item in items:
            if type(item) == list:
                for i in item:
                    self.item_list.append(i)
            else:
                self.item_list.append(item)
    
    def remove_items(self, *items):
        for item in items:
            if type(item) == list:
                for i in item:
                    self.item_list.remove(i)
            else:
                self.item_list.remove(item)