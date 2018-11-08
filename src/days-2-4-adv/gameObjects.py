# Write a class to hold player information, e.g. what room they are in
# currently.
import random

class Object:
	def __init__ (self,name,room):
		self.room = room
		self.name = name

	def __str__ (self):
		return"{}, currently in room {}".format(self.name, self.room)
		
class Player(Object):
	def __init__(self,name,hp,mp,attack,defence,clas):
		super().__init__(name,"cheesy beginnings")
		self.clas = clas
		self.MaxHp = hp
		self.CurHp = hp
		self.MaxMp = mp
		self.CurMp = mp
		self.attack = attack
		self.defence = defence
		self.invientory = []
		
	def __str__(self):
		return "{}, the {}\nhp: {}/{}\nmp: {}/{}\nattack bouns: {}\ndefence bonus: {}".format(self.name,self.clas,self.CurHp,
		self.MaxHp,self.CurMp,self.MaxMp,self.attack,self.defence)
		
class Monster(Object):
	def __init__(self,name,hp,attack,defence,lines,enter,death,drops,room):
		super().__init__(name,room)
		self.MaxHp = hp
		self.CurHp = hp
		self.attack = attack
		self.defence = defence
		self.lines = lines
		self.enter = enter
		self.death = death
		self.drops = drops
		
	def __str__(self):
		return "A {}\nhp: {}/{}".format(self.name,self.CurHp,self.MaxHp)
		
	def enter(self):
		return "{}".format(self.enter)
	def death(self):
		return "{}".format(self.death)
	def talk(self):
		n = random.randint(0, len(self.lines)-1)
		print (self.lines[n])