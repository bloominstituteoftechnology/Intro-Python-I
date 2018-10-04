# Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap

class Player():
        def __init__(self,name,room):
                self.name=name
                self.currentRoom=room
                self.score=0
                self.treasure={'gold':0, 'silver':0, 'ruby':0}
                #self.silver=0
                #self.ruby=0
                self.items=[]

        def room_name(self):
                return f'Your current location is: {self.currentRoom.name}'

        def addItem(self, item):
                self.items.append(item)

        def removeItem(self, item):
                if len(self.items) > 0:
                        for i in self.items:
                                if i.name==item:
                                        self.items.remove(i)
                                        return True
                else:
                        print('The item you are trying to drop is not present in your inventory')
        
        def showItems(self):
                if len(self.items) > 0:
                        for i in self.items:
                                print(f'{i}')  
                else:
                        print(f'No items')    

        def addScore(self,itemAtt,value):
                if self.treasure[itemAtt]==0:
                        self.score=self.score+value
                        self.treasure[itemAtt]=1
                        print(f'Your new score is {self.score}')
                else:
                        print('Your score will not increse on adding this item')
                    
        def travel(self, direction):
                nextRoom = None
                if direction == "n":
                        if self.currentRoom.n_to is not None:
                                nextRoom = self.currentRoom.n_to
                elif direction == "s":
                        if self.currentRoom.s_to is not None:
                                nextRoom = self.currentRoom.s_to
                elif direction == "e":
                        if self.currentRoom.e_to is not None:
                                nextRoom = self.currentRoom.e_to
                elif direction == "w":
                        if self.currentRoom.w_to is not None:
                                nextRoom = self.currentRoom.w_to
                if nextRoom is not None:
                        self.currentRoom = nextRoom
                        print(nextRoom)
                else:
                        print("You cannot move in that direction.")


