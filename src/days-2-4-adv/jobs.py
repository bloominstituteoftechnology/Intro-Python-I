class Job:
    def __init__(self, name, attack, vitality, intelligence, dexterity, wisdom):
        self.name = name
        self.attack = attack
        self.vitality = vitality
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.wisdom = wisdom


jobs = {
    'Warrior': Job('Warrior', 28, 10, 10, 15, 5),
    'Mage': Job('Mage', 25, 15, 25, 10, 25),
    'Thief': Job('Thief', 15, 20, 10, 25, 5)
}
