# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
        def __init__(self, name, text, items):
                self.name=name.split(' ', 1)[0].lower()     
                self.text=text
                self.n_to=None
                self.s_to=None
                self.e_to=None
                self.w_to=None
                self.items=items

        
        
        def __str__(self):
            return f'You are in: {self.name} and the author has a message for you: {self.text}'

        def showItems(self):
                if (self.items):
                        for i in self.items:
                                print(f'{i.name}')
                else:
                        print('No itmes available')    

        def addItem(self,item):
                self.items.append(item)

        def getItem(self, itemIn):
                allItems=[]
                if len(self.items) > 0:
                        for i in self.items:
                                if i.name==itemIn:
                                    return i.name                                    
                else:
                        return None

        def removeItem(self, item):
                if len(self.items) > 0:
                        for i in self.items:
                                if i.name == item:
                                        self.items.remove(i)
                else:
                        print('Item not available to remove!')
            

                            
