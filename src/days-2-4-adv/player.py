# Write a class to hold player information, e.g. what room they are in
# currently.
Class Player:
    def __init__(self, room):
        self.room = room
    def __str__(self):
        return f"Currently in room: {self.room}" 
