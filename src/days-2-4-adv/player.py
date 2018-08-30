# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room, score):
        self.name = name
        self.room = room
        self.bag = []
        self.score = 0
    def takeItem(self, item):
        self.bag.append(item)
        # print(self.bag)
    def check_bag(self):
        if len(self.bag) == 0:
            print('Bag is empty')
        else:
            print('Bag has: ')
            # for c, value in enumerate(self.bag, 1):
            #     print (str(c) + str(value))
            return ', '.join([item for item in self.bag])
    def dropItem(self, item):
        if len(self.bag) is 0:
            print('Bag is empty')
        else:
            for item in self.bag:
                self.items.remove(item)
    def currentScore(self):
        print(self.score)




    def moveTo(self, direction):
        self.direction = direction