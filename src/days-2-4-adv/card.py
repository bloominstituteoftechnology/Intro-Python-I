# card class
from item import Item

class Card:
    def __init__(self, name, description, deck, level=None, attack=None, defence=None, card_type=None, element=None, effects=None):
        self.name = name
        self.description = description
        self.deck = deck
        self.card_type = card_type
        self.element = "Dark" if element is None else element
        self.level = 1 if level is None else level
        self.defence = 0 if defence is None else defence
        self.attack = 0 if attack is None else attack
        self.effects = [] if effects is None else effects

    # class methods

    # discard method to discard a card
    def discard(self, item):
        del self.items[self.items.index(item)]


    # check the cards effect list for a specific effect
    def check_for_effect(self, effect_name):
        for effect in self.effects:
            if effect.name == effect_name:
                return True
        return False

    def __str__(self):
        return str(self.name)  + "\n" + str(self.description)