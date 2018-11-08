# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, title, current_room):
        self.title = title
        self.current_room = current_room
        self.inventory = []

    def move(self, getDir):
        key = getDir + '_to'

        if not hasattr(self.current_room, key):
            print('Wrong way!')
            return self.current_room
        else:
            return getattr(self.current_room, key)

    # def move(self, getDir):
    #     if getDir == 'q':
    #         print('See you later!')
    #     if self.current_room == 'outside':
    #         if getDir == 'n':
    #             self.current_room = 'foyer'
    #         else:
    #             print('Wrong direction, please re-input!')
    #     elif self.current_room == 'foyer':
    #         if getDir == 'n':
    #             self.current_room = 'overlook'
    #         elif getDir == 'e':
    #             self.current_room = 'narrow'
    #         else:
    #             print('Wrong direction, please re-input!')
    #     elif self.current_room == 'overlook' or self.current_room == 'treasure':
    #         if getDir == 's':
    #             self.current_room = 'foyer'
    #         else:
    #             print('Wrong direction, please re-input!')
    #     else:
    #         print('Please input valid direction!')
        



        


    