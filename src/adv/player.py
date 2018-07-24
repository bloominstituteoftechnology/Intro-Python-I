# Write a class to hold player information, e.g. what room they are in currently.

class Player:
    def __init__(self, playerName, room):
        self.playerName = playerName
        self.room = room

    def playerDetails(self):
        return 'Player {} is in the {}'.format(self.playerName, self.room)

player_1 = Player('Anthony', 'Bedroom')

print(player_1.playerDetails())
