# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room, score=0):
        self.inRoom = room
        self.items = []
        self.score = score

    def move(self, room):
        self.inRoom = room

    def addItem(self, item):
        self.items.append(item)
        print(f"You picked up {item.name}")

    def dropItem(self, item):
        item.on_drop()
        self.items.remove(item)

    def showItmes(self):
        print('You are holding the following: ')
        for item in self.items:
            print(item.name)

    def showScore(self):
        print(f"Your score is {self.score}")
