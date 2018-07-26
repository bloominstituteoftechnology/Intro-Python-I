# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, playername, room):
		self.room = room
		self.inventory = []
		self.name = playername

	def showInventory(self):
		return self.inventory

	def showRoom(self):
		return self.room

	def updateRoom(self, dest):
		self.room = dest

	def showAllItems(self):
		for item in self.inventory:
			print("\t{0}\n".format(item.name))