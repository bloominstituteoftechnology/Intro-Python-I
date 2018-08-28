# Implement a class to hold room information. This should have name and
# description attributes.

#Put the Room class in room.py based on what you see in `adv.py`.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description



location1 = Room('Living Room', 'Space for lounging and hanging out.')

print(location1.name)
print(location1.description)