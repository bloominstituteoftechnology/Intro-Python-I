class Item:
    # str, Room(class reference)
    #{name: 'Jackee', location: SOME OBJECT REFERENCE}
        def __init__(self, name, description):
            self.name = name
            self.description = location
        def move_to(self, direction):
            cardinal = direction + '_to'
            try:
                if getattr(self.location, cardinal):
                    #move towards it --->
                    self.location = self.location.__dict__[cardinal]
            except AttributeError:
                if direction == 'q':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Thank you for playing..')
                    sleep(1)
                    os._exit(0)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\nPick a different option, You cannot go that way...')
                sleep(3)