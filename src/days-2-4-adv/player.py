# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.contents = []
        self.score = 0

p = Player("Cat", "Room 1")
print(p.name)
print(p.room)