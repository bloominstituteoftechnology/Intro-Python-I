# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap

class Room():
        def __init__(self, name, text):
                self.name=name.split(' ', 1)[0].lower()     
                self.text=text
                self.next_d=None

        def text_descr(self):
                return f'{textwrap.fill({self.text}, 35)}'       

        def connecting(self, direction, next_destination):
                if self.name =='outside' and direction =='n':
                        self.next_d=next_destination.name
                elif self.name =='foyer' and direction =='s':
                        self.next_d=next_destination.name
                elif self.name =='foyer' and direction =='n':
                         self.next_d=next_destination.name
                elif self.name =='foyer' and direction =='e':
                         self.next_d=next_destination.name
                elif self.name =='overlook' and direction =='s':
                         self.next_d=next_destination.name
                elif self.name =='narrow' and direction =='w':
                         self.next_d=next_destination.name
                elif self.name =='treasure' and direction =='s':
                         self.next_d=next_destination.name
                else:
                         self.next_d=self.name
                    
    
                    
    

