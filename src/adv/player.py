# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, player, room):
        self.player = player
        self.room = room

    def printPlayer(self):
        return f"{self.player} is in the {self.room}"


# test = Player("Bob", "kitchen")

# print(test.printPlayer())