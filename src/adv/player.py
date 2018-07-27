from lightsource import LightSource
from printing import prompt
from weapon import Weapon
from commandparser import quit_game

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []
        self.fist = Weapon(5, "fist", ["knobbly"], "It's all you've got")
        self.last_item = ''
        self.health = 100
        self.score = {
            'items': 0,
            'monsters': 0
        }

    def has_item(self, item_name):
        return item_name in [item.name for item in self.items]
    
    def get_item(self, item_name):
        return [item for item in self.items if item.name == item_name][0]

    def remove_item(self, item):
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)

    def take_item(self, item_name):
        item = self.room.get_item(item_name)
        if item.on_take(self):
            self.room.remove_item(item)
            self.add_item(item)

    def drop_item(self, item_name):
        item = self.get_item(item_name)
        if item.on_drop(self):
            self.remove_item(item)
            self.room.add_item(item)

    def can_see(self):
        return self.room.is_illuminated() or self.has_light_source()

    def has_light_source(self):
        return len([item for item in self.items if isinstance(item, LightSource)]) > 0

    def get_score(self):
        return sum(self.score.values())

    def add_score(self, category, amount):
        self.score[category] += amount

    def attack(self, monster_name):
        monster = self.room.get_monster(monster_name)
        prompt(f"{self} swings at the {monster} with their {self.get_weapon()}.")

        if monster.on_attack(self):
            # Remove monster from the game if we've killed it
            self.room.remove_monster(monster)
        else:
            monster.retaliate(self)

    def apply_damage(self, amount):
        if amount >= self.health:
            prompt(f"{self} has suffered a mortal wound!")
            quit_game()
        else:
            prompt(f"{self} suffers {amount} points of damage!")
            self.health -= amount

        
    def get_attack_damage(self):
        return self.get_weapon().damage

    def get_weapon(self):
        weapons = [item for item in self.items if isinstance(item, Weapon)]
        if weapons:
            # use the weapon with the highest damage
            weapon = sorted(weapons, key=lambda weapon: weapon.damage, reverse=True)[0]
            return weapon

        return self.fist

    def __str__(self):
        return self.name
