class Item:
    def __init__(self, name, description, equippable=None):
        self.name = name
        self.description = description
        self.equippable = False if equippable is None else True
        self.equipped = False

    def on_pickup(self):
            raise NotImplementedError

    def on_drop(self):
            return 'Y'

# create a KEY subclass that can unlock doors when picked up

# create a LIGHTSOURCE subclass that can illuminate dark places

class LightSource(Item):
    def __init__(self, name, description, equippable=True):
        self.name = name
        self.description = description

    def on_drop(self):
        print(f'Dropping your light source will leave you in darkness!')
        decision = input('Are you sure you want to do this? (Y/N)')
        if decision.upper() == 'Y':
            return decision.upper()
        elif decision.upper() == 'N':
            return decision.upper()
        else:
            print(f'That is not a valid command.')
            return 'N'