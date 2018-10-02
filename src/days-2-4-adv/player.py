# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self,name):
        self.name = name
        self.currentRoom= ""
    def __str__(self):
        return f"\n{self.currentRoom}\n{priorRoom} - {self.losses} - {self.ties}\n"
    def roomMove(self, move):
        if result == 1:
            self.wins += 1
        elif result == 0:
            self.ties += 1
        elif result == -1:
            self.losses += 1
