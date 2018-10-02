# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(myRoom,name,description):
        myRoom.name = name
        myRoom.description = description
        myRoom.currentRoom= 0
        myRoom.priorRoom = 0

    def __str__(myRoom):
        return f"\n{myRoom.name}\n{myRoom.currentRoom} - {myRoom.priorRoom}\n"
   # def roomMove(myRoom, move):

