# Implement a class to hold room information. This should have name and
# description attributes.

# Add functionality to the main loop that prints out all the items that are visible to the player when they are in that room.
class Room:
    def __init__(self, locationName, locationDescription):
        self.name = locationName
        self.description = locationDescription

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.description!r})')
# Add capability to add items to rooms.
# The Room class should be extended with a list that holds the Items that are currently in that room.






# location1 = Room('Living Room', 'Space for lounging and hanging out.')
# # print("Location name: " + location1.name + "\n" + "Location description: " + location1.description)

# print(repr(location1))
