class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

item = {
    'outside':  Item("flashlight",
                     "You find a flashlight. It probably belonged to someone else. Surprisingly, the batteries still work."),

    'foyer':    Item("rock", """You've decided to pickup an ordinary rock."""),

    'overlook': Item("axe", """You found a bloodstained axe. Someone either used it to defend themselves in their final moments
    or was attacked from behind."""),

    'narrow':   Item("bone", """The found the remains of someone."""),

    'treasure': Item("pouch", """An empty pouch."""),
}


item['outside'].n_to = item['foyer']
item['foyer'].s_to = item['outside']
item['foyer'].n_to = item['overlook']
item['foyer'].e_to = item['narrow']
item['overlook'].s_to = item['foyer']
item['narrow'].w_to = item['foyer']
item['narrow'].n_to = item['treasure']
item['treasure'].s_to = item['narrow']