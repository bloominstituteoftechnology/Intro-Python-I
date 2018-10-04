class Weapon():
    def __init__(self, label, name, discription):
        self.name = name
        self.discription = discription
        self.label = label
                

    def __repr__(self):
        return f'{self.name}: {self.discription}'


class Grenade(Weapon):
    def __init__(self, name, discription):
        super().__init__(name, discription)

# class Frag(Grenade):
#     def __init__()
