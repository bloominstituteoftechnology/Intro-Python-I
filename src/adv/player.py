
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def grab(self, item):
        for item in self.room.items:
            if item.name == item:
                self.items.append(item)
                self.room.items.remove(item)
                return
            else:
                ### what do i put here if i dont grab the item but want to keep going?


    def drop(self, item):
        for item in self.items:
            if item.name == item: 
                self.room.items.append(item)
                self.items.remove(item)
                return
            else:
                ### what do i put here
