class Item(dict):
    def __init__(self, name, description):
      self[name] = name
      self[description] = description

