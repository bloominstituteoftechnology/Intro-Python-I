
class Item:
    #constructor
    def __init__(self, name, description):
        self.name = name
        self.description = description
    #string method. Returns something 
    #when converted to a string
    def __str__(self):
        return self.name  

    def __repr__(self):
        return self.name