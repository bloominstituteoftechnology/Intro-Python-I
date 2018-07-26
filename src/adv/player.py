class Player:
    def __init__(self, startRoom, name):
        self.name = name
        self.currentRoom = startRoom
        self.inventory = []
        self.hp = 100