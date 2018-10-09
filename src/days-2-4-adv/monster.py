class Monster:
    def __init__(self, name, description, monsterCurrentRoom, inventory, attack):
        self.name = name
        self.description = description
        self.monsterCurrentRoom = monsterCurrentRoom
        self.inventory = inventory
        self.health = 100
        self.attack = attack