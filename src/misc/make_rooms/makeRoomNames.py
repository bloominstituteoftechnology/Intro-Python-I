import os
import sys
import random


with open(os.path.join(sys.path[0], 'ingredients.txt'), 'r') as f:
    ingredients = f.read().split("\n")

with open(os.path.join(sys.path[0], 'rooms.txt'), 'r') as f:
    places = f.read().split("\n")


with open(os.path.join(sys.path[0], 'adjectives.txt'), 'r') as f:
    adjectives = f.read().split("\n")


for i in range(10):
    adjective = adjectives[random.randint(0, len(adjectives) - 1)]
    ingredient = ingredients[random.randint(0, len(ingredients) - 1)]
    place = places[random.randint(0, len(places) - 1)]
    print(f'The {adjective.upper()} {ingredient.title()} {place.title()}')
