from room import Room

RoomList = {
  'outside': Room(
    "Outside Cave Entrance",
    "North of you, the cave mount beckons",
    None
  ),
  'foyer': Room(
    "Foyer",
    """Dim light filters in from the south. Dusty passages run north and east.""",
    None
  ),
  'overlook': Room(
    "Grand Overlook",
    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
    None
  ),
  'narrow': Room(
    "Narrow Passage",
    """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
    None
  ),
  'treasure': Room(
    "Treasure Chamber",
    """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
    None
  ),
}

RoomList['outside'].n_to = RoomList['foyer']
RoomList['foyer'].s_to = RoomList['outside']
RoomList['foyer'].n_to = RoomList['overlook']
RoomList['foyer'].e_to = RoomList['narrow']
RoomList['overlook'].s_to = RoomList['foyer']
RoomList['narrow'].w_to = RoomList['foyer']
RoomList['narrow'].n_to = RoomList['treasure']
RoomList['treasure'].s_to = RoomList['narrow']