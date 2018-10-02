# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,currentLocation):
        self.location=currentLocation
        self.inventory=[]
    def __str__(self):
        return f'location: {self.location}'
    def travel(self,location):
        self.location=location