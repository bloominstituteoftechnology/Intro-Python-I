class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def on_take(self):
        print(f"You've picked up {self.name}!")
        return 0

    def on_drop(self):
        print(f"You've dropped {self.name}!")

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def on_take(self):
        if (self.value!=0):
            print(f"Congratulations! You're the first finder of the treasure {self.name}! You got {self.value} points!")            
        else:
            print(f'This treasure {self.name} has been found before. You got no point!')
        return self.value
    
    def on_drop(self):
        print(f"You've dropped {self.name}!")
        self.value = 0

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print(f"It's not wise to drop your source of light!!")

        
