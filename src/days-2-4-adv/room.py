# Implement a class to hold room information. This should have name and
# description attributes.


class Room (object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    def __repr__(self):
        return f"Room Name: {self.name}, Room description: {self.description}"
