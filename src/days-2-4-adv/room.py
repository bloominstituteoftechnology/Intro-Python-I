# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,name,description):
        self.name=name
        self.description=description
        self.inventory=[]
    def __str__(self):
        itemArr=[]
        for item in self.inventory:
            itemArr.extend(item.name)
        itemArr=', '.join(itemArr)
        return f'name: {self.name}\ndescription: {self.description}\nitems available: {itemArr}'