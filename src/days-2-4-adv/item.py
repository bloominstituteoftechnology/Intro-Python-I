class Item():
        def __init__(self, name, description):
                self.name=name
                self.description=description

        def __str__ (self):
                return(f'{self.name}')
        
        def on_take(self):
            print(f'You have added a new item to your list: {self.name}')

        def on_drop(self):
            print(f'You have dropped the item from your list: {self.name}')    

class Treasure(Item):
        def __init__(self, name, description, value):  
                Item.__init__(self, name, description)
                self.value=value
                        
        def on_take(self):
                pass
