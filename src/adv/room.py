# Implement a class to hold room information. This should have name and description attributes.

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.n_to = None
    self.s_to = None
    self.w_to = None
    self.e_to = None
<<<<<<< HEAD

  def __repr__(self):
    return "%s" % (self.name)
=======
>>>>>>> 0ab68d6bc3a3d95fde8b9dc6c86efe2fa46f8f91
