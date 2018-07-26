from textwrap import wrap

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.bound = None
    
    def info(self):
        info_message = self.name + ':\t' + self.description
        return '\n'.join(wrap(info_message, width=50))+ '\n' + '-'*50
    
    def on_take(self, player):
        return 1

    def on_drop(self, player):
        return 1

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
    
    def on_take(self, player):
        player.score = player.score + self.value
        return 1
    
    def on_drop(self, player):
        player.score = player.score - self.value
        return 1

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.lit = True
    
    def on_drop(self,player):
        # Loops until valid input is provided
        while(True):
            print('\n'*50)
            print("It's not wise to drop your source of light!" )
            print('Pick from one of the options to decide')
            choice = input('Drop (yes/no)? | (y/n)?')
            if choice in ['yes', 'y']:
                # if the choices are yes, y
                return 1
            elif choice in ['no', 'n', '']:
                # if the chices are no, n or just pressed enter
                return 0
