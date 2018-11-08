from item import Item, Weapon, Shield, Armour, Treasure, Lightsource
from items import items
from player import Monster

# Initialize all the monsters
slime = Monster()
slime.name = 'Slime'
slime.description = 'Slimey slime'
slime.attack = 5
slime.exp = 10
slime.gold = 10
slime.hp = 50
slime.inventory = [items['Book']]
slime.dead = False

bat = Monster()
bat.name = 'Bat'
bat.description = 'A dark nat'
bat.attack = 5
bat.exp = 10
bat.gold = 10
bat.hp = 50
bat.inventory = []
bat.dead = False

monsters = {'Slime': slime, 'Bat': bat}
