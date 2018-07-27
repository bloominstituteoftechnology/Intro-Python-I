
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

    #on_take method
    def __on_take__(self):
        print(f'{self.name} has been picked up!')

class Treasure:
    def __init__(self, name, description, value):
        super().__init__()
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return self.name  

    def __repr__(self):
        return self.name

    def __onTake__(self):
        print("Treasure value has been added to score!")

    def __onDrop__(self):
        print("Treasure value has been removed from score!")