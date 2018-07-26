# base class for all specialized in game items

class Item:
	def __init__(self, name, description):
		self.name = name # one word
		self.description = description
		
	def showName(self):
		return self.name

	def showDescription(self):
		return self.description

	def on_take(self, entity, item_name):
		# called when player picks up an item
		# Item uses this to run more code when picked up
		return "{0} picked up the {1} and put in in their inventory". format(entity.name, item_name)

	def on_drop(self, entity, item_name):
		# called when player drops an item
		return "{0} dropped the {1} in the {2}".format(entity.name, item_name, entity.room.name)

class Treasure(Item):
	def __init__(self, name, description, value):
		super().__init__(name, description)
		self.value = value

	def on_take(self, entity, treasure_name):
		# get value of Treasure added to player's score
		# occurs on first pick up only
		entity.score += self.value
		self.value = 0
		return "{0} picked up the {1}, a rare treasure.".format(entity.name, treasure_name) 