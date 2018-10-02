# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.skill = 0

    def __str__(self):
        return f"\n{self.name}\n{self.wins} - {self.losses}\n {self.name} has a skill rating of: {self.skill} "

    def addResult(self, result):
        if result == 1:
            self.wins += 1
            self.skill = (self.wins - self.losses) / 4
            if self.skill < 0:
                self.skill = 0
        elif result == -1:
            self.losses += 1
            self.skill = (self.wins - self.losses) / 4
            if self.skill < 0:
                self.skill = 0
