# Add an Item class
# with name and description attributes..

class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # these prints for on_take() and on_drop basically repeat the print on if inp[0] == 'take' or 'drop'
    def on_take(self):
        print('You\'ve picked up the %s' % (self.name))

    def on_drop(self):
        print('You\'ve dropped the %s' % (self.name))

def __repr__(self):
    return f"{self.name} - {self.description}"

class Treasure(Items):
    def __init__(self, name, description, value, dropped):
        self.name = name
        self.description = description
        self.value = value
        self.dropped = False

class Lightsource(Items):
    def __init__(self, name, description):
        self.name = name
        self.description = description