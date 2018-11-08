

class Weapon:
    def __init__(self, name, description, damage_type, bonus_damage=None):
        self.name = name
        self.description = description
        self.damage_type = damage_type
        self.bonus_damage = bonus_damage
