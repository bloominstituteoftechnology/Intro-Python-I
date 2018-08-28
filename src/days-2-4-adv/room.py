# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return self.name
    def getDescription(self):
        wrapper = textwrap.TextWrapper(initial_indent="* ", width=40, subsequent_indent="* ")
        return wrapper.fill(self.description) + "\n"
    def validMoves(self):
        valid = {}
        if self.n_to:
            valid.update(N = self.n_to)
        if self.s_to:
            valid.update(S = self.s_to)
        if self.e_to:
            valid.update(E = self.e_to)
        if self.w_to:
            valid.update(W = self.w_to)
        return valid