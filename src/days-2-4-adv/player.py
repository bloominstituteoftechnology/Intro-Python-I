# Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap

class Player():
        def __init__(self,room):
                self.room=room

        def room_name(self):
                return f'Your current room is: {self.room}'
        
