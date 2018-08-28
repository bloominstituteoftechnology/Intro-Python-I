# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location):
        self.location = location

    def printLoc(self):
        print('I am player1 and I am {}'.format(self.location))
        #return 'I am player1 and I am {}'.format(self.location)

    def move(self, destination):
        self.location = destination
        print('I moved to the {}'.format(self.location))
