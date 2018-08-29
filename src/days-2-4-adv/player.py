# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.bag = []
    def takeItem(self, item):
        self.bag.append(item)
        print(item + ' is in your bag')
    def check_bag(self):
        if len(self.bag) == 0:
            print('Bag is empty')
        else:
            for c, value in enumerate(self.bag, 1):
                print(c, value)




    def moveTo(self, direction):
        self.direction = direction