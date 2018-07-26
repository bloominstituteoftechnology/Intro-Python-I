class Npc:
  def __init__(self, name, description = ''):
    self.name = name
    self.description = description

class Mob(Npc):
  def __init__(self, name, description = '', reqItem = [], vanquished = False):
    Npc.__init__(self, name, description)
    self.reqItem = reqItem
    self.vanquished = vanquished