# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, shortname, items):
        self.name = name
        self.shortname = shortname
        self.description = description
        self.n_to = None
        self.w_to = None
        self.s_to = None
        self.e_to = None
        self.items = items
        
    def view_items(self):
        if len(self.items) is not 0:
            print("You found something! Too collect, press a number. \n")
            for i, e in enumerate(self.items):
                print(str(i) + "-" + e)
            print("A-All")
        else:
            print("There is nothing here")
    
    def remove_item(self, index):
        del self.items[index]