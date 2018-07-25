# Write a class to hold player information, e.g. what room they are in
# currently.

from time import sleep
import os


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
