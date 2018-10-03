# Implement a class to hold room information. This should have name and
# description attributes. 

class Room (object):
    
    def __init__(self, name, description,items = [], n_to = None, s_to = None, e_to = None, w_to = None):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.directions = [] 

    def __str__(self):
        return f"Room Name: {self.name}\n\n, Room description: {self.description}\n\n"
    def revealItems(self):
        items = []
        for item in self.items:
            items.append((item.name, f"description {item.description}"))
        return (f"This room includes the following: {items}\n\n to pick up these items use keyword grab item_name\n\n")
    def change_room(self, option):
        if option == "n" and self.n_to is not None:
            return self.n_to
        elif option == "s" and self.s_to is not None:
            return self.n_to
        elif option == "w" and self.w_to is not None:
            return self.w_to
        elif option == "e" and self.e_to is not None:
            return self.e_to
        else:
            return None
    #
    def removeItem(self,item):
        if self.items.count(item) > 0:
            self.items.remove(item)
            return(f"{item.name} has been removed from the {self.name}\n\n to drop an item use drop item_name\n \n to check your inventory use  i\n\n")
        else:
            return None
    def addItem(self, item):
        self.items.append(item)


    #
    #
    #
    #
    #
    #
    #
