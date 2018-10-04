class Item:
    def __init__(self, name, description):
        # starting class attributes
        self.name = name
        self.description = description
    def __repr__(self): # __repr__ displays objects similar to strings 
        return f"\n\n{self.name}\n\n {self.description}\n"
        # return f string with the item name and description separated by whitespace.