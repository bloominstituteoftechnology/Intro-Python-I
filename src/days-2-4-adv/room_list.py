"""
template:
    '<key_name>': {
        'name': '<name>',
        'description': '<description>',
        'is_light': <True or False>
        'exits': <(tuple of 'n', 'e', 's', 'w')>
        'exits_for': <(tuple opposite of exits entries)>
    }
"""

rooms = {
    'North': {
        'name': 'N Room',
        'description': """Room with a North Exit""",
        'is_light': True,
        'exits': ('n',),
        'exits_for': ('s',)
    },
    'South': {
        'name': 'S Room',
        'description': """Room with a South Exit""",
        'is_light': True,
        'exits': ('s',),
        'exits_for': ('n',)
    },
    'East': {
        'name': 'E Room',
        'description': """Room with an East Exit""",
        'is_light': True,
        'exits': ('e',),
        'exits_for': ('w',)
    },
    'West': {
        'name': 'W Room',
        'description': """Room with a West Exit""",
        'is_light': True,
        'exits': ('w',),
        'exits_for': ('e',)
    },
    'North-East': {
        'name': 'NE Room',
        'description': """Room with North and East Exits""",
        'is_light': True,
        'exits': ('n', 'e'),
        'exits_for': ('s', 'w')
    },
    'North-South': {
        'name': 'NS Room',
        'description': """Room with North and South Exits""",
        'is_light': True,
        'exits': ('n', 's'),
        'exits_for': ('s', 'n')
    },
    'North-West': {
        'name': 'NW Room',
        'description': """Room with North and West Exits""",
        'is_light': True,
        'exits': ('n', 'w'),
        'exits_for': ('s', 'e')
    },
    'East-South': {
        'name': 'ES Room',
        'description': """Room with East and South Exits""",
        'is_light': True,
        'exits': ('e', 's'),
        'exits_for': ('w', 'n')
    },
    'East-West': {
        'name': 'EW Room',
        'description': """Room with East and West Exits""",
        'is_light': True,
        'exits': ('e', 'w'),
        'exits_for': ('w', 'e')
    },
    'South-West': {
        'name': 'SW Room',
        'description': """Room with South and West Exits""",
        'is_light': True,
        'exits': ('s', 'w'),
        'exits_for': ('n', 'e')
    },
    'North-East-West': {
        'name': 'NEW Room',
        'description': """Room with North, East, and West Exits""",
        'is_light': True,
        'exits': ('n', 'e', 'w'),
        'exits_for': ('s', 'w', 'e')
    },
    'North-East-South': {
        'name': 'NES Room',
        'description': """Room with North, East, and South Exits""",
        'is_light': True,
        'exits': ('n', 'e', 's'),
        'exits_for': ('s', 'w', 'n')
    },
    'North-South-West': {
        'name': 'NSW Room',
        'description': """Room with North, South, and West Exits""",
        'is_light': True,
        'exits': ('n', 's', 'w'),
        'exits_for': ('s', 'n', 'e')
    },
    'East-South-West': {
        'name': 'ESW Room',
        'description': """Room with East, South, and West Exits""",
        'is_light': True,
        'exits': ('e', 's', 'w'),
        'exits_for': ('w', 'n', 'e')
    },
    'North-East-South-West': {
        'name': 'NESW Room',
        'description': """Room with North, East, South, and West Exits""",
        'is_light': True,
        'exits': ('n', 'e', 's', 'w'),
        'exits_for': ('s', 'w', 'n', 'e')
    }
}

# needed for a test
# def print_rooms():
#     for room in rooms:
#         print(rooms[room])
# print_rooms()
