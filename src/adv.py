rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "n_to": "foyer",
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "s_to": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.",
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "s_to": "narrow",
    },

}


class TextUtilities:
    def print_title(self, title):
        title_sep = ''.center(len(title), '-')
        print('\n{}\n{}'.format(title, title_sep))

    def print_description(self, description):
        print('{}\n'.format(description))
    
    def print_error(self, message):
        message_wrapper = ''.center(len(message) + 4, '!')
        print('\n{1}\n! {0} !\n{1}'.format(message, message_wrapper))

    def print_list_of_dicts(self, list):
        for item in list:
            for key, val in item.items():
                print('[{}] {}'.format(key, val))


class Player:
    def __init__(self, location):
        self.text_util = TextUtilities()
        self.location = location
    
    def get_available_directions(self):
        available_directions = []
        for attr in rooms[self.location]:
            if attr.endswith("_to"):
                direction = attr.replace("_to", "")
                room = rooms[self.location][attr]
                available_directions.append({direction:room})
        return available_directions
    
    def look(self):
        self.text_util.print_title(rooms[self.location]["name"])
        self.text_util.print_description(rooms[self.location]["description"])
        self.text_util.print_title("Available Directions")
        self.text_util.print_list_of_dicts(self.get_available_directions())

    def move(self, command):
        direction = command + '_to'
        try:
            self.location = rooms[self.location][direction]
        except KeyError:
            self.text_util.print_error("Whoops, that's not a valid direction")


class GameObject:
    def __init__(self):
        self.player = Player("outside")
        self.text_util = TextUtilities()
        self.play = True
        self.command = ''
        self.commands = {
            "n": self.player.move,
            "s": self.player.move,
            "e": self.player.move,
            "w": self.player.move,
            "q": self.quit_game
        }
        self.start_game()

    def start_game(self):
        self.text_util.print_description("\n*** And so our story begins... ***")
        while self.play:
            self.player.look()
            self.get_command()

    def quit_game(self, command):
        self.play = False
        self.text_util.print_description("\n*** Goodbye ***")
    
    def get_command(self):
        self.command = input("\nWhat do you want to do? ")
        self.process_command()

    def process_command(self):
        try:
            self.commands[self.command](self.command)
        except KeyError:
            self.text_util.print_error("Not sure what you mean")

game = GameObject()
