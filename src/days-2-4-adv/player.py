# Write a class to hold player information, e.g. what room they are in
# currently.


class Player: 
    def __init__(self, currentRoom, items):
        self.currentRoom = currentRoom
        self.items = items
    def add(self, item):
        self.items.append(item)
    def remove(self, item):
        if len(self.items) > 0:
            for i in self.items:
                if i.name == item:
                    self.items.remove(i)
        else:
            print("item not avalible")
