# Implement a class to hold room information. This should have name and
# description attributes.
import random


class Room:

    def __init__(self, title, desc, itemDrop):
        self.title = title
        self.desc = desc
        self.droppedItem = None
        self.itemDrop = itemDrop
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
            return f"\n\n--{self.title}-- \n{self.desc} \n"
     
