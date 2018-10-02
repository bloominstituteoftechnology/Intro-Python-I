# Implement a class to hold room information. This should have name and
# description attributes.
from player import Player

class Room():
    def _init_(self,name,description):
        self.name = name
        self.description = description
    def _printName_(self):
        print(self.name)
    def _printDescription_(self):
        print(self.description)


