# Implement a class to hold room information. This should have name and
# description attributes.

class Links:
	def __init__(self,dir,room,vis):
		self.links = list(zip(dir,room,vis))
	
	def __str__(self):
		return"{}".format(self.links)

class Room(Links):
	def __init__(self, values):
		super().__init__(values[2],values[3],values[4])
		self.name = values[0]
		self.desc = values[1]
	def __str__(self):
		return "Room: {}: {}".format(self.name,self.desc)