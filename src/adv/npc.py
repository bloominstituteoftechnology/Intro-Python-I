class Npc:
  def __init__(self, name, description = ''):
    self.name = name
    self.description = description

class Mob(Npc):
  def __init__(self, name, description = '', vanquished = False):
    Npc.__init__(self, name, description)
    self.vanquished = vanquished

class Follower(Npc):
  def __init__(self, name, description = '', following = False):
    Npc.__init__(self, name, description)
    self.following = following