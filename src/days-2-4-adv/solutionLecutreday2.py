class Room:
    error_msg = "You cannot move in that direction!"
    #^May want to put this in the player
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None 
    def travel(self, direction): 
        pass 
        #put in changes here. 
#What is the difference between an object and a class?
""" class creates objects  object is an instance of a class 
    a class is like a receipe different incredients
    like a user every user will have a name a password what data
    was created first last name phone number a instance of a user is a row
    but the class would be the table of users or the ability to add rows
    while the class defines the columns.

    namespaces are  from room import Room 
    seperate code as much as possible.  Namespaces are one honking great idea 
    lets use more of those.  - zen of python. 

      """
suppressRoomPrint = False 
player = Player(input("What is your name? ", room['outside']))
directions = {}
while True:
    if suppressRoomPrint:
        suppressRoomPrint = False 
    else:
        print(player.currentRoom.name + "\n" + player.currentRoom.description)
    cmd = input("-> ")
    if cmd == 'q':
        break
    elif cmd == "n" or cmd == "s" or cmd == "e" or cmd == "w": 
        # run the function to change rooms
        pass 
    elif cmd == "n":
        if player.currentRoom.n_to is not None: 
            player.currentRoom = player.currentRoom.n_to
            suppressRoomPrint = True  
    elif cmd == "s":
       if player.currentRoom.s_to is not None:
           player.currentRoom = player.currentRoom.s_to
           suppressRoomPrint = True
    elif cmd == "w":
        if player.currentRoom.w_to is not None: 
            player.currentRoom = player.currentRoom.w_to
            suppressRoomPrint = True
    elif cmd == "e":
        if player.currentRoom.e_to is not None:
            player.currentRoom = player.currentRoom.e_to 
            suppressRoomPrint = True
    else:
        print("I did not understand that command.")  
x = "a b c"
x.split("")
cmds = input("-> ").split(" ")
#now we have to reference cmds[0]
if len(cmds) == 1:
    pass
    #handle all one item commands 
else:
    if cmds[0] == "look":
        # do something
        pass
    else: 
        print("I did not understand that command.")

def getRoomInDirection(self, direction):
    return self.n_to #etc.. 