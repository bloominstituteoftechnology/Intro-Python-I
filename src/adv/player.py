# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, name, curRoom, inventory):
		self.name = name
		self.room = curRoom
		self.inventory = inventory

	def addToInventory(self, item):
		for i in range (len(self.room.itemList)):
			print(i)
			if self.room.itemList[i].name == item:
				print(self.room.itemList[i].description)
				self.inventory.append(self.room.itemList[i])
				del self.room.itemList[i]
				break

	def check_map(self):
		print("North: " + (self.room.n_to.name if self.room.n_to else "Nothing.") +
			"\nSouth: " + (self.room.s_to.name if self.room.s_to else "Nothing.") +
			"\nEast: " + (self.room.e_to.name if self.room.e_to else "Nothing.") +
			"\nWest: " + (self.room.w_to.name if self.room.w_to else "Nothing."))