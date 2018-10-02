class Item (object):
    def __init__(self, name, description): 
        self.name = name 
        self.description = description
    def __repr__(self):
        return f"The item name is {self.name}. Description : {self.description}."