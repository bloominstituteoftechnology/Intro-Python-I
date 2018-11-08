# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
	def __init__(self,name,location, inventory = []):
		self.name = name
		self.location = location
		self.inventory = inventory

	def try_move(self, direction):
		d = direction + "_to"

		if not hasattr(self.currentRoom, d):
			print("You can't go that way!")
			return self.currentRoom
		else:
			self.currentRoom = getattr(self.currentRoom, d)

	def pickup_item(self, item):
		self.inventory.append(item)

	def drop_item(self, item):
		self.inventory.remove(item)