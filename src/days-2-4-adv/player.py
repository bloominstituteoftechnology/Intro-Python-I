# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(player, name):
        player.name = name

    def greet(player):
        print(f"{player.name} greeted you")

    # not @classmethod: call a method on an instance
    # player = Player(...)
    # player.create(...)
    #
    # @classmethod: call a method on a class
    # Player.create(...)
    @classmethod
    def create(cls, name, kind):
        if kind == "hunter":
            return PlayerType1(name)
        elif kind == "mage":
            return PlayerType2(name)
        else:
            # cls = Player
            return cls(name)