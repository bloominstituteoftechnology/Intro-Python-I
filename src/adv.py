rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "items": ["lamp", "sword"],
        "n_to": "foyer",
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        "items": [],
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "items": [],
        "s_to": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.",
        "items": [],
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "items": [],
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
    
    def print_list(self, list):
        for item in list:
            print('[{}]'.format(item))

    def print_list_of_dicts(self, list):
        for item in list:
            for key, val in item.items():
                print('[{}] {}'.format(key, val))


class Player:
    def __init__(self, location):
        self.text_util = TextUtilities()
        self.location = location
        self.inventory = []
    
    def look(self, level):
        level[self.location].print_room_description()
        level[self.location].print_room_items()
        level[self.location].print_available_directions()

    def move(self, command, command_attr):
        direction = command + '_to'
        try:
            self.location = rooms[self.location][direction]
        except KeyError:
            self.text_util.print_error("Whoops, that's not a valid direction")
    
    def take(self, command, command_attr):
        print("player takes an item")


class Room:
    def __init__(self, id, room):
        self.text_util = TextUtilities()
        self.id = id
        self.room_obj = room
        self.directions = self.get_available_directions()

    def get_available_directions(self):
        available_directions = []
        for attr in self.room_obj:
            if attr.endswith("_to"):
                direction = attr.replace("_to", "")
                room = self.room_obj[attr]
                available_directions.append({direction: room})
        return available_directions

    def print_room_description(self):
        self.text_util.print_title(self.room_obj["name"])
        self.text_util.print_description(self.room_obj["description"])
    
    def print_room_items(self):
        items = self.room_obj["items"]
        self.text_util.print_title("Items in Room")
        if len(items) == 0:
            print("<none>")
        else:
            self.text_util.print_list(items)

    def print_available_directions(self):
        self.text_util.print_title("Available Directions")
        self.text_util.print_list_of_dicts(self.directions)


class GameObject:
    def __init__(self, rooms):
        self.text_util = TextUtilities()
        self.player = Player("outside")
        self.level = self.build_level(rooms)
        self.command = ''
        self.command_attr = ''
        self.commands = {
            "n": self.player.move,
            "s": self.player.move,
            "e": self.player.move,
            "w": self.player.move,
            "take": self.player.take,
            "q": self.quit_game
        }
        self.play = True
        self.start_game()

    def build_level(self, rooms):
        level = {}
        for room in rooms:
            level[room] = Room(room, rooms[room])
        return level

    def start_game(self):
        self.text_util.print_description("\n*** And so our story begins... ***")
        while self.play:
            self.player.look(self.level)
            self.get_command()

    def quit_game(self, command, command_attr):
        self.play = False
        self.text_util.print_description("\n*** Goodbye ***")
    
    def get_command(self):
        self.parse_command(input("\nWhat do you want to do? "))
        self.process_command()

    def parse_command(self, input):
        player_input = input.lstrip().rstrip().lower().split()
        if len(player_input) == 1:
            self.command = player_input[0]
            self.command_attr = ''
        elif len(player_input) == 2:
            self.command = player_input[0]
            self.command_attr = player_input[1]
        else:
            self.command = ''
            self.command_attr = ''

    def process_command(self):
        try:
            self.commands[self.command](self.command, self.command_attr)
        except KeyError:
            self.text_util.print_error("Not sure what you mean")

game = GameObject(rooms)
