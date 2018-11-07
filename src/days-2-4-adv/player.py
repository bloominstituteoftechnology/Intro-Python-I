# Write a class to hold player information, e.g. what room they are in
# currently.

class Object:
	def __init__ (self,name):
		self.room = "cheesy beginnings"
		self.name = name

	def __str__ (self):
		return"{}, currently in room {}".format(self.name, self.room)
		
class Player(Object):
	def __init__(self,name,hp,mp,attack,defence,clas):
		super().__init__(name)
		self.clas = clas
		self.MaxHp = hp
		self.CurHp = hp
		self.MaxMp = mp
		self.CurMp = mp
		self.attack = attack
		self.defence = defence
		
	def __str__(self):
		return "{}, the {}\nhp: {}/{}\nmp: {}/{}\nattack bouns: {}\ndefence bonus: {}".format(self.name,self.clas,self.CurHp,
		self.MaxHp,self.CurMp,self.MaxMp,self.attack,self.defence)