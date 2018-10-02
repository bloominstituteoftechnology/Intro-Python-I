# Write a class to hold player information, e.g. what room they are in
# currently.

import random
from room import Room

defaultRoom = 'outside'


class Player():
    def __init__(self, name):
        self.name = name
        self.room = defaultRoom
