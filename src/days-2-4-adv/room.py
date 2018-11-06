# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,name,descr):
     self.name = name
     self.descr = descr

    def __str__(self):
        return f'{self.name}:\n{self.description}.'

    