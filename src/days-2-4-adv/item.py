class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def on_take(self):
        print(f"You've picked up {self.name}!")

    def on_drop(self):
        print(f"You've dropped {self.name}!")

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def on_take(self):
        if (self.value!=0):
            print(f"Congratulations! You're the first finder of the treasure {self.name}! You got {self.value} points!")
            score = self.value
            self.value = 0
            return self.value
        else:
            print(f'This treasure {self.name} has been found before. You got no point!')


        
