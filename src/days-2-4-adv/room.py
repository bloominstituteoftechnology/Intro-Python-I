# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, location, description, is_light):
        self.location = location
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
        self.is_light = is_light

    def __str__(self):
        return f'{self.location}: {self.description}'

    def get_room(self, dir):
      if dir == 'n':
        return self.n_to
      if dir == 'e':
        return self.e_to
      if dir == 's':
        return self.s_to
      if dir == 'w':
        return self.w_to
      else:
        return None

    def examine(self, has_light):
      if self.is_light or has_light:
        print(self.__str__())
        if len(self.items) > 0:
          print('You notice in this room: ')
          for item in self.items:
            print(item)
        else:
          print("You see nothing of interest in this room")
      else:
        print("It's too dark to see anything!")

    def list_exits(self, has_light):
      if self.is_light or has_light:
        exits = []
        if self.n_to is not None:
          exits.push('(N)orth')
        if self.e_to is not None:
          exits.push('(E)ast')
        if self.s_to is not None:
          exits.push('(S)outh')
        if self.w_to is not None:
          exits.push('(W)est')
        print('The current exits are: ')
        for exit in exits:
          print(exit)
      else:
        print("It's too dark to see any exits, trying going back the way you came!")
