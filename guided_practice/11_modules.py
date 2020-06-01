"""
Modules
"""
# each module has a specific functionality and is a different file

# # 1. import command
import game.py
import draw 

# # game.py
# # import the draw module
# import draw

def play_game():
     pass

def main():
     result = play_game()
     draw.draw_game(result)

 # draw.py

def draw_game():
     pass

def clear_screen(screen):
     pass

# # 2. from command
# # game.py
#  import the draw module
from draw import draw_game

def main():
     result = play_game()
     draw_game(result)

# # 3. import *
# # game.py
# # import the draw module
from draw import *

def main():
     result = play_game()
     draw_game(result)

# # 4. import as
# # game.py
# # import the draw module
if visual_mode:
#     # in visual mode, we draw using graphics
     import draw_visual as draw
else:
     # in textual mode, we print out text
     import draw_textual as draw

def main():
     result = play_game()
     # this can either be visual or textual depending on visual_mode
     draw.draw_game(result)

# # 5. dir and help
# # Just show fiddling around with help and dir in the terminal