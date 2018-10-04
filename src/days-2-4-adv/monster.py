class Monster:
    def __init__(self, name, description, currentRoom, inventory, attack):
        self.name = name
        self.description = description
        self.currentRoom = currentRoom
        self.inventory = inventory
        self.health = 100
        self.attack = attack