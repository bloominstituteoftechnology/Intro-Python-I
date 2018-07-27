from printing import prompt

class Monster:
    def __init__(self, name, description, health, damage):
        self.name = name
        self.description = description
        self.health = health
        self.damage = damage
    
    def on_attack(self, player):
        return self.apply_damage(player.get_attack_damage())

    def apply_damage(self, amount):
        if amount >= self.health:
            prompt(f"The {self} has been slain!")
            return True

        prompt(f"The {self} suffers {amount} points of damage!")
        self.health -= amount
        return False

    def retaliate(self, player):
        prompt(f"The {self} strikes back in anger!")
        player.apply_damage(self.damage)

    def __str__(self):
        return self.name
