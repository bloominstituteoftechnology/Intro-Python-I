
class Item:
	def __init__(self, item_type, item_descr, is_being_used):
		self.item_type = item_type
		self.item_descr = item_descr
		self.isPickedUp = False
		self.isUsed = False
		self.isBeingUsed = is_being_used
	
	def setIsPickedUp(self):
		self.isPickedUp = True if (self.isPickedUp == False) else False

	def setIsUsedUp(self):
		self.isUsed = True if (self.isUsed == False) else False

	def getItemType(self):
		return self.item_type

	def getItemDescription(self):
		return self.item_descr

	def getBeingUsed(self):
		return self.isBeingUsed