# base class for all specialized in game items

class Item:
	def __init__(self, name, description):
		self.name = name # one word
		self.description = description
		
	def showName(self):
		return self.name

	def showDescription(self):
		return self.description

class Treasure(Item):
	def __init__(self, name, description, value):
		super().__init__(name, description)
		self.value = value