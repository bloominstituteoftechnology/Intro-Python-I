
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def on_take(self):
    print(f'You picked up {self.name}!!!')
def on_drop(self):
    print(f'You have dropped {self.name}!!!')


class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value



