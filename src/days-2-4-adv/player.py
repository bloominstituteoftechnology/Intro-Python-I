# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        #health
        #inv

    def printStatus(self):
        print('*****************************')
        print(self.name)
        #health
        #items
        self.location.printRoom()
