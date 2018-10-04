class Monster:
    def __init__(self,name,description,greet):
        self.name=name
        self.description=description
        self.greet=greet
    def on_attack(self):
        return f'{self.greet}'