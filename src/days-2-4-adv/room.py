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
                return f'{self.name} {self.text}'

        def showItems(self):
                if (self.items):
                        for i in self.items:
                                return(f'{i.name}')

        def addItem(self,item):
                self.items.append(item)

        def getItem(self, item):
                if(self.items):
                        for i in self.item:
                                if i==item:
                                        return i   
                else:
                        return None

        def removeItem(self, item):
                self.items.remove(item)

                
                    
                            
