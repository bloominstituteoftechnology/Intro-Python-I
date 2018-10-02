# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(room, name, description):
        room.name = name
        room.description = description

    # not @classmethod: call a method on an instance
    # room = Room(...)
    # room.create(...)
    #
    # @classmethod: call a method on a class
    # Room.create(...)
    @classmethod
    def create(cls, name, kind):
        if kind == "outside":
            return OutsideRoom(name, description)
        elif kind == "foyer":
            return FoyerRoom(name, description)
        elif kind == "overlook":
            return OverlookRoom(name, description)
        elif kind == "narrow":
            return NarrowRoom(name, description)
        elif kind == "treasure":
            return TreasureRoom(name, description)