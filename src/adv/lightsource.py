from item import Item
from printing import prompt
from commandparser import bool_prompt

class LightSource(Item):
    def __init__(self, *args):
        super().__init__(*args)

    def on_drop(self, player):
        if bool_prompt(f"{player} is about to drop their light source!", "Continue? (yes/no): "):
            return super().on_drop(player)
        else:
            prompt(f"Not dropping the {self}.")
            return False
