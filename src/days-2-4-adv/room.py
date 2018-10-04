# Implement a class to hold room information. This should have name and
# description attributes. 

class Room (object):
    
    def __init__(self, name, description,items = [],treasure = None, is_light = None ):#n_to = None, s_to = None, e_to = None, w_to = None
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.treasure = treasure
        self.directions = [] 
        self.is_light = is_light

    def __str__(self):
        return f"Room Name: {self.name}\n\n, Room description: {self.description}\n\n Room has light : {self.is_light}"
    def revealItems(self):
        items = []
        for item in self.items:
            items.append((item.name, f"description {item.description}"))
        return (f"This room includes the following: {items}\n\n to pick up these items use keyword grab item_name\n\n")
    def getDirections(self):
        return f"n: {self.n_to},\n\n s: {self.s_to},\n\n e: {self.e_to},\n\n w: {self.w_to}\n\n"
    def change_room(self, option):
        print(f"n: {self.n_to},\n\n s: {self.s_to},\n\n e: {self.e_to},\n\n w: {self.w_to}\n\n")#debug purposes
        if option == "n" and self.n_to is not None:
            print("n : You chose to go north")
            return self.n_to
        elif option == "s" and self.s_to is not None:
            print("s : You chose to go south")
            return self.s_to
        elif option == "w" and self.w_to is not None:
            print("w You chose to go west")
            return self.w_to
        elif option == "e" and self.e_to is not None:
            print("e You chose to go east")
            return self.e_to
        else:
            return None
    
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
