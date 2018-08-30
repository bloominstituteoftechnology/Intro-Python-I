class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player):
        print(f'Picked up {self.name}!')

    def on_drop(self):
        print(f'\x1b[1;31;40m\nDropped {self.name}\x1b[0m')

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        self.looted = False

    def on_take(self, player):
        if not self.looted:
            player.score += self.value
            print(f'\x1b[1;31;40m\nYou picked up {self.name} and earned {self.value} score!\x1b[0m')
            self.looted = True
        else:
            print(f'\x1b[1;31;40m\nYou picked up {self.name} but do not earn any score because you have already looted this item.\x1b[0m')