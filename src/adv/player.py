# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, player, room, inventory, score):
        self.player = player
        self.room = room
        self.inventory = inventory
        self.score = score

    def printPlayer(self):
        return f"{self.player} is in the {self.room}"


# test = Player("Bob", "kitchen")

# print(test.printPlayer())