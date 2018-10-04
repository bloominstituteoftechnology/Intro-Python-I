# Write a class to hold player information, e.g. what room they are in
# currently.


class Player: 
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.score = 0
        self.items = []
    def add(self, item):
        self.items.append(item)
    def removeItem(self, item):
        if len(self.items) > 0:
            for i in self.items:
                if i == item:
                    self.items.remove(i)
        else:
            print("item not avalible")
    def find(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None 
    def menu(self):
        if len(self.items) > 0:
            for item in self.items:
                print(item.name)
        else:   
            print("No items")
    def playerScore(self):
        print(f"Score: {self.score}")
        
            
    

    #add a menu so that the player can see what they have in their inventory
    # def menu(self):
    #     for item in self.items:
    #         print(item.name)