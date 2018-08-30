# Implement a class to hold room information. This should have name and
# description attributes.

#"Put the Room class in room.py based on what you see in `adv.py`."

class Room:
    def __init__(self, locationName, locationDescription):
        self.name = locationName
        self.description = locationDescription

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.description!r})')

# location1 = Room('Living Room', 'Space for lounging and hanging out.')
# # print("Location name: " + location1.name + "\n" + "Location description: " + location1.description)

# print(repr(location1))
