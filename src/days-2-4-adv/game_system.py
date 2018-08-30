class Game_System:
    @staticmethod
    def display_help():
        print("""
        Type in a command:

        Directions[n,s,e,w]

        Get info: [look for items, look for enemies, check inventory]

        Battle: [a [Enemy]: attack [Enemy]]

        Other commands: [q: quit]
        """)