class Item (object):
    def __init__(self, name, description): 
        self.name = name 
        self.description = description
    def __repr__(self):
        return f"The item name is {self.name}. Description : {self.description}."

class Treasure(Item):
    def __init__(self,value, name, description):
        self.value = value
        super(Treasure,self).__init__(name, description)