# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f" {self.name}"
    # def __getitem__(self, key):
    #     return super(Room, self).__getitem__(key-1)