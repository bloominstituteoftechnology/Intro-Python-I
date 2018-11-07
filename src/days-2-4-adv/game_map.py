

class Map:
    @staticmethod
    def game_map(current_room):
        if current_room == "Outside Cave Entrance":
            print("""              XXXXXXXX XXX XXXXX
            XXXX XX XXXXXXXX XX XXXXXX
           XXXX XXXXXXXXXX XXXX   XXXX
           XX          XXXXX         X
              +----------------+
              |  Overlook      |
              +------+ +-------+
                     | |
                     | |           +------------+
                     | |           |  Treasure  |
                     | |           |            |
                     | |           +----+ +-----+
                 +---+ +----+           | |
                 |  Foyer   +-----------+ | <---- Narrow
                 |          +-------------+
                 +---+  +---+
XXXXXXXXXX           |  |             XXXXX
         XXXXXXXXXXXX+  +XXXXXXXXXXXXXX

                    Outside
                       #
You are the '#' symbol!
""")
        elif current_room == "Foyer":
            print("""              XXXXXXXX XXX XXXXX
            XXXX XX XXXXXXXX XX XXXXXX
           XXXX XXXXXXXXXX XXXX   XXXX
           XX          XXXXX         X
              +----------------+
              |  Overlook      |
              +------+ +-------+
                     | |
                     | |           +------------+
                     | |           |  Treasure  |
                     | |           |            |
                     | |           +----+ +-----+
                 +---+ +----+           | |
                 |  Foyer   +-----------+ | <---- Narrow
                 |    #     +-------------+
                 +---+  +---+
XXXXXXXXXX           |  |             XXXXX
         XXXXXXXXXXXX+  +XXXXXXXXXXXXXX

                    Outside
You are the '#' symbol!
""")
        elif current_room == "Narrow Passage":
            print("""              XXXXXXXX XXX XXXXX
            XXXX XX XXXXXXXX XX XXXXXX
           XXXX XXXXXXXXXX XXXX   XXXX
           XX          XXXXX         X
              +----------------+
              |  Overlook      |
              +------+ +-------+
                     | |
                     | |           +------------+
                     | |           |  Treasure  |
                     | |           |            |
                     | |           +----+ +-----+
                 +---+ +----+           | |
                 |  Foyer   +-----------+#| <---- Narrow
                 |          +-------------+
                 +---+  +---+
XXXXXXXXXX           |  |             XXXXX
         XXXXXXXXXXXX+  +XXXXXXXXXXXXXX

                    Outside
You are the '#' symbol!
""")
        elif current_room == "Treasure Chamber":
            print("""              XXXXXXXX XXX XXXXX
            XXXX XX XXXXXXXX XX XXXXXX
           XXXX XXXXXXXXXX XXXX   XXXX
           XX          XXXXX         X
              +----------------+
              |  Overlook      |
              +------+ +-------+
                     | |
                     | |           +------------+
                     | |           |  Treasure  |
                     | |           |     #      |
                     | |           +----+ +-----+
                 +---+ +----+           | |
                 |  Foyer   +-----------+ | <---- Narrow
                 |          +-------------+
                 +---+  +---+
XXXXXXXXXX           |  |             XXXXX
         XXXXXXXXXXXX+  +XXXXXXXXXXXXXX

                    Outside
You are the '#' symbol!
""")
        elif current_room == "Grand Overlook":
            print("""              XXXXXXXX XXX XXXXX
            XXXX XX XXXXXXXX XX XXXXXX
           XXXX XXXXXXXXXX XXXX   XXXX
           XX          XXXXX         X
              +----------------+
              |  Overlook   #  |
              +------+ +-------+
                     | |
                     | |           +------------+
                     | |           |  Treasure  |
                     | |           |            |
                     | |           +----+ +-----+
                 +---+ +----+           | |
                 |  Foyer   +-----------+ | <---- Narrow
                 |          +-------------+
                 +---+  +---+
XXXXXXXXXX           |  |             XXXXX
         XXXXXXXXXXXX+  +XXXXXXXXXXXXXX

                    Outside
You are the '#' symbol!
""")