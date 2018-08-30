   prompt = input("Are you sure you want to quit?: ")
        if yesNo(prompt) = true:
            break
        else:
            print("Continuing game")
    
    def yesNo(x):
    if x = "yes":






class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def getRoominDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None
        
        while True:
            print(f'\n {player.location.name}\n {player.location.description}\n')
            inp = input("What is your command: ")
            if inp == "q":
                break
            if inp == "n" or if inp == "s" or if inp == "e" or if inp == "w":
                newRoom = player.location.getRoomInDirection(inp)
                if newRoom == "None":
                    print ("Cannot move in that direction")
                player.change_location()

                room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']