
class Items:
    def __init__(self, name, description, itemType):
        self.name=name
        self.description=description
        self.itemType=itemType
    

class Food(Items):
    def __init__(self, health):
        super().__init__(self, name, description, itemType)
        self.health = random.randint(health[0], health[1])
        self.currentHealth = self.health
        
    def eat(self,item):
        
