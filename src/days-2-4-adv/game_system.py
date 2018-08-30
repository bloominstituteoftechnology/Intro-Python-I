class Game_System:
    @staticmethod
    def display_help():
        print("""
    'n': partial(player.go_direction, 'n'),
    's': partial(player.go_direction, 's'),
    'e': partial(player.go_direction, 'e'),
    'w': partial(player.go_direction, 'w'),
    'help': display_help,
    'hp': player.get_hp,
    'health': player.get_hp,
    'my': {
        'health': player.get_hp,
        'hp': player.get_hp
    },
    'q': quit,
    'quit': quit,
    'loc': player.get_current_location,
    'look':{
        'for': {
            'items': player.look_for_items,
            'enemies': player.look_for_enemies
        },
        'around': player.get_current_location
    },
    'where': {
        'am': {
            'i': player.get_current_location
        },
        'is': {
            'this': {
                'place': player.get_current_location
            }
        }
    },
    'check':{
         'inventory': player.get_inventory,
    },
    'inventory': player.get_inventory,
    'get': {
        'item': player.add_item,
        'hp': player.get_hp,
        'current': {
            'location': player.get_current_location
        }
    },
    'grab': {
        'item': player.add_item
    },
    'drop': {
        'item': player.drop_item
    }
        """)