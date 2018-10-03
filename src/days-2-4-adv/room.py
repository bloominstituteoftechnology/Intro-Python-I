# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self,name,description,items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def printName(self):
        print(self.name)
    def printDesc(self):
        print(self.description)
    def printItems(self):
            for item in self.items:
                print(item.name, "--", item.description)
    def find(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None  
    def add(self, item):
        self.items.append(item)
    def remove(self, item):
        if len(self.items) > 0:
            for i in self.items:
                if i.name == item:
                    self.items.remove(i)
        else:
            print("item not avalible")



