# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
	"""docstring for ClassName"""
	def __init__(self, name, description, items = []):
		self.name = name
		self.description = description
		self.items = items
	
	n_to = None
	s_to = None
	w_to = None
	e_to = None

	def add_items(self, items):
		self.items += items




