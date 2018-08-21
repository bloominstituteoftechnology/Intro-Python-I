# Implement a class to hold zone information. This should have name and
# description attributes.
from random import randint

class GameEntity:
    def __init__(self, name='', description=''):
        self.name = name
        self.description = description

class World:
    """Contains and links the rooms"""
    def connect():
        pass

class Zone(GameEntity):
    def __init__(self, name='', description='', cardinals={'north': None, 'south': None, 'east': None, 'west': None}):
        GameEntity.__init__(self, name, description)
        self.cardinals = cardinals
        self.target = self

    def updateLinks(self, north=None, south=None, east=None, west=None):
        """Please provide key values for the four cardinal directions, you may ignore falsy entrys."""
        updated = {
            'north': north if north != None else self.cardinals['north'],
            'south': south if south != None else self.cardinals['south'],
            'east': east if east != None else self.cardinals['east'],
            'west': west if west != None else self.cardinals['west']
            }

        self.cardinals.update(updated)

    # def move(self, player, direction):
    #     if self.cardinals[direction] == None:
    #         print('You are blocked by a wall.')
    #     else:
    #         player.zone = self.cardinals[direction]
    #         print(player.zone.name)

class Player(GameEntity):
    def __init__(self, name='', description='', zone=None):
        GameEntity.__init__(self, name, description)
        self.stats = { 'attack': 20, 'accuracy': 10, 'evasion': 10, 'agility': 1, 'defence': 1, 'hp': 100 }
        self.target = self
        self.zone = zone

    def move(self, direction):
        check = self.zone.cardinals[direction]
        if check == None:
            print('You are blocked by a wall.')
        else:
            self.zone = check
            print(self.zone.name)


    def attack(self, target=None):
        """evaluate if hit, call targets defend()"""
        if target == None:
            target = self.target
        if (randint(0, self.stats['accuracy'] >= target.stats['evasion'])):
            target.defend(self.stats['attack'])
        else:
            print('whiff')

    def defend(self, damage):
        """Takes int value and does not care about the source."""
        self.stats['hp'] -= randint(0, damage - self.stats['defence']) # This is an effective means of taking damage off the top
        print(self.stats['hp'])


z1 = Zone('desert', 'idk')
z2 = Zone('ice level', 'everyone hates this level')
s1 = { 'west': z2 }
s2 = { 'east': z1 }
z1.updateLinks(**s1)
z2.updateLinks(**s2)
p1 = Player('Jahi', 'Jahi was a Galka I played in FFXI. The better part of a decade off and on.', z1)
p2 = Player('Eman', 'Eman is my EVE Online character. Wormhole corp. Quick with a scan.')
p1.attack(p2)
p2.attack(p1)
p1.move('west')
print(p1.zone.name)
p1.move('west')
print(p1.zone.name)
p1.move('east')
print(p1.zone.name)
p1.move('east')
print(p1.zone.name)
p1.move('west')
print(p1.zone.name)
p1.move('west')
print(p1.zone.name)
