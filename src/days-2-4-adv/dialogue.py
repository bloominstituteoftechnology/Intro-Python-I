class Dialogue:
    @staticmethod
    def intro():
        print("""
        Welcome New Adventurer
        You will encounter many dangers,
        first lets setup your character
        """)
    @staticmethod
    def greet_player(name):
        print(f"""
        Hi {name}, you are our last hope.
        We must prepare you for the hardships that come your way.
        We will place you outside a training ground to hone your skills.
        Type 'help' to see the command list to find your abilities.
        You are on your own. Good luck!
        """)
        