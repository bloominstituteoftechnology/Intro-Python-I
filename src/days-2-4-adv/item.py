# Item Class


class Item:
	def __init__(self, name, description = ""):
		if len(name.split()) > 1:
			raise Exception("Name must be a single word")
		self.name = name
		self.description = description

	def __string__(self):
		return self.name

	def on_take(self):
		input(f"You took {self.name}. Please Enter to continue.")

	def on_drop(self):
		input(f"You dropped {self.name}. Please Enter to continue.")



