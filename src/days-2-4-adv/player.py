# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, currentRoom):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.skill = 0
        self.currentRoom = currentRoom

    def __str__(self):
        return f"\n{self.name}\n{self.wins} - {self.losses}\nSkill Rating: {self.skill} "

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


    def movement(self, direction):
        # print("hiiii", self.currentRoom)
        nextRoom = self.currentRoom.directedRoom(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(nextRoom)
        else:
            print("*Runs into a shiny purple wall*")    

    def look(self, direction=None):
        if direction is None:
            print(self.currentRoom)
        else:
            nextRoom = self.currentRoom.directedRoom(direction)
            if nextRoom is not None:
                print(nextRoom)
            else:
                print("Just a wall. Try elsewhere")        
