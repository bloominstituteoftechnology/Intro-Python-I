class Item():
        def __init__(self, name, description):
                self.name=name
                self.description=description

        def __str__ (self):
                return(f'{self.name}')
        
        def on_take(self):
            print(f'You have added a new item to your list: {self.name}')

        def on_drop(self):
            print(f'You have dropped {self.name} from your list')    

class Treasure(Item):
        def __init__(self, name, description, value):  
                Item.__init__(self, name, description)
                self.value=value
                        
        def on_take(self):
                return self.value

        def on_drop(self):
                pass
        

class LightSource(Item):
        def __init__(self, name, description):
                Item.__init__(self, name, description)
        
        def on_take(self):
                pass

        def on_drop(self):
                print("It's not wise do drop your source of light!")
