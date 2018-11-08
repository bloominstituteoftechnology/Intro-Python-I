from item import Item, Weapon, Shield, Armour, Treasure, Lightsource

items = {
    'EmptyW': Weapon('Empty Slot', ' '),
    'EmptyS': Shield('Empty Slot', ' '),
    'EmptyA': Armour('Empty Slot', ' '),
    'EmptyL': Item('Empty Slot', ' '),

    'Sword': Weapon('Sword', 'A simple sword', 20, 10, 5, 10, 2, 5, 1),
    'Stick': Weapon('Stick', 'A small stick. This doesn\'t look like it will do much damage', 5),
    'Wooden Sword': Weapon('Wooden Sword', 'A step above a stick', 20, 2, 3, 3, 0, 3, 0),
    'Apprentice Staff': Weapon('Wooden Sword', 'A step above a stick', 20, 15, 25, 10, 5, 25, 10),

    'Rusty Shield': Shield('Rusty Shield', 'A small rusty shield', 5, 10),

    'Peasant Clothes': Armour('Peasant Clothes', 'Holey clothing for peasants', 0, 10),

    'Potion': Item('Potion', 'A health potion'),

    'Book': Treasure('Book', 'A dirty old book', 50),

    'Lamp': Lightsource('Lamp', 'A bight lamp')
}
