class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

        def __str__(self):
            return self.name

        def __repr__(self):
            return self.name


class Treasure(Item):
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

        def on_take():
            print('The treasure was taken')