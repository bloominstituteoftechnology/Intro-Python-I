# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,currentLocation):
        self.location=currentLocation
        self.possessions=[]
    def __str__(self):
        return f'location: {self.location}'
    def travel(self,location):
        self.location=location
    def pickup(self,item):
        self.possessions.append(item)
    def i(self):
        itemArr=', '.join(self.possessions)
        return f'Items currently in possession: {itemArr}'
    def inventory(self):
        itemArr=', '.join(self.possessions)
        return f'Items currently in possession: {itemArr}'