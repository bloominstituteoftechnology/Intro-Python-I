# Implement a class to hold room information. This should have name and
# description attributes.

class Links:
	def __init__(self,key,value):
		self.links = list(zip(key,value))
	
	def __str__(self):
		return"{}".format(self.links)

class Room(Links):
	def __init__(self, name, desc, key, value):
		super().__init__(key, value)
		self.name = name
		self.desc = desc
	def __str__(self):
		return "Room: {}: {}".format(self.name,self.desc)