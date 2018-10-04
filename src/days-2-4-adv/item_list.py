from item import Item, Treasure, LightSource

starter_lantern = LightSource('Lantern', 'Adding while testing')

items = [
    Treasure('Helmet', "A bronze helmet. Slightly dented, but still intact", 250),
    Treasure('Bracers', 'Leather bracers. May cause chafing', 100),
    Treasure('Pants', 'Will DEFINITELY cause chafing', 300),
    Treasure('Chestpiece', 'Strong iron chestpiece', 750),
    Treasure('Sword', 'Slightly dull, but will lay some hurt', 500),
    Item('Tome', 'Maybe someone will pay for this'),
    Item('Fork', 'Looks to be silver plated and thus worthless, why take it?'),
    LightSource('Torch', 'Good for light AND setting things on fire!')
]
