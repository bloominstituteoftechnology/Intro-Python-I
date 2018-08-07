# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.bag = []
        
    def add_item(self, item):
        self.bag.append(item)
        
    def view_bag(self):
        print("\n In your bag:")
        if len(self.bag) is not 0:
            for e in self.bag:
                print(e)
        else:
            print("Your bag is empty")
    
    def getRoom(self):
        print('***********************************')
        print('You are in: ' + self.room.name)
        print('This room is: ' + self.room.description)