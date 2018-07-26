class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self): # creates string representation of obj
        return self.name 

    def __repr__(self): # dispays the object 
        return self.name