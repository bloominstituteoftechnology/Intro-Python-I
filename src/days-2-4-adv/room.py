# Implement a class to hold room information. This should have name and
# description attributes.

# Add capability to add items to rooms.The Room class should be extended with a list that holds the Items that are currently in that room.

class Room:
    def __init__(self, locationName, locationDescription, locationItems=None):
        if locationItems is None:
            locationItems = []
        self.name = locationName
        self.description = locationDescription
        self.items = locationItems

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.description!r}, {self.items!r})')



# l1 = Room('basement', 'a space for storing items', ['pen', 'pencil', 'skateboard'])
# print(l1.items)



# location1 = Room('Living Room', 'Space for lounging and hanging out.')
# # print("Location name: " + location1.name + "\n" + "Location description: " + location1.description)

# print(repr(location1))
