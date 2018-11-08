# Item Class


class Item:
	def __init__(self, name, description):
		if len(name.split()) > 1:
			raise Exception("Name must be a single word")
		self.name = name
		self.description = description


