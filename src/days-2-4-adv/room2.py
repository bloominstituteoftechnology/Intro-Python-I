# Implement a class to hold room information. This should have name and
# description attributes.

from items import Items


class Room(Items):

    def __init__(self, room_name="Outside Cave Entrance", room_description="North of you, the cave mount beckons"):
        super().__init__()
        self.room_name = room_name
        self.room_description = room_description


    def __str__(self):
        return "<Room - Name: %s, Description: %s, Items: %s >" % (self.room_name, self.room_description, self.items_list)

#
# r = Room("name", 'desc')
# r.add_item({'x': 'xx'})
#
# print(r.__str__())