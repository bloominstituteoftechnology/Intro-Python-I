# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, job, location):
        self.name = name
        self.job = job
        self.location = location
        self.currentRoom = None
