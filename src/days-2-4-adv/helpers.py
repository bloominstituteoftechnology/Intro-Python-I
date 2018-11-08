from gameObjects import Player,Monster
import random

def char_creator(pn):
	while True:
		pclass = input("Choose a class! Warrior, berserker, wizard, sorcerer, rouge\n\n> ")
		if pclass == "warrior":
			while True:
				ran1 = random.randint(0, 6)	# I'll be using... 5 of these. So expect a bunch of horrid looking code.
				ran2 = random.randint(0, 6)	# stat generator. Probably can be pulled into a different file later.
				ran3 = random.randint(1, 3)	# going to look sloppy, but I'll need to customize each class
				ran4 = random.randint(1, 2)	# at least a little, so they look different when displayed
				if ran1+ran2+ran3+ran4 >= 13:
					break
			hp = ran1+14
			mp = ran2+4
			attack = ran3+2		#for now, I'll just adjust numbers added to the random generated stats.
			defence = ran4+2
			p = Player(pn,hp,mp,attack,defence,"warrior")
			return p
			break
		elif pclass == "berserker":
			while True:
				ran1 = random.randint(0, 6)	# 
				ran2 = random.randint(0, 6)	# 
				ran3 = random.randint(1, 3)	# 
				ran4 = random.randint(1, 2)	# 
				if ran1+ran2+ran3+ran4 >= 13:
					break
			hp = ran1+10
			mp = ran2+2
			attack = ran3+4
			defence = ran4+1
			p = Player(pn,hp,mp,attack,defence,"berserker")
			return p
			break
		elif pclass == "wizard":
			while True:
				ran1 = random.randint(0, 6)	# 
				ran2 = random.randint(0, 6)	# right now, spells DNE, caster classes
				ran3 = random.randint(1, 3)	# will be WEAK until more features are added
				ran4 = random.randint(1, 2)	# 
				if ran1+ran2+ran3+ran4 >= 13:
					break
			hp = ran1+8
			mp = ran2+12
			attack = ran3+1
			defence = ran4+1
			p = Player(pn,hp,mp,attack,defence,"wizard")
			return p
			break
		elif pclass == "sorcerer":
			while True:
				ran1 = random.randint(0, 6)	# 
				ran2 = random.randint(0, 6)	# see wizard
				ran3 = random.randint(1, 3)	# 
				ran4 = random.randint(1, 2)	# 
				if ran1+ran2+ran3+ran4 >= 13:
					break
			hp = ran1+12
			mp = ran2+8
			attack = ran3+1
			defence = ran4+1
			p = Player(pn,hp,mp,attack,defence,"sorcerer")
			return p
			break
		elif pclass == "rouge":
			while True:
				ran1 = random.randint(0, 6)	# 
				ran2 = random.randint(0, 6)	# a bit spell dependant,
				ran3 = random.randint(1, 3)	# but also probably item dependant class
				ran4 = random.randint(1, 2)	# likely will just be unplayable.
				if ran1+ran2+ran3+ran4 >= 13:
					break
			hp = ran1+14
			mp = ran2+4
			attack = ran3
			defence = ran4+2
			p = Player(pn,hp,mp,attack,defence,"rouge")
			return p
			break
		else:
			print("\nsorry, did you misspell that?\n")
			
def Monster_Creator(monster,room):
	while True:
		ran1 = random.randint(0, 5)
		ran2 = random.randint(0, 2)
		ran3 = random.randint(0, 2)
		if ran1+ran2+ran3 >= 5:
			break
	hp = ran1+int(monster[1])
	attack = ran2+int(monster[2])
	defence = ran3+int(monster[3])
	m = Monster(monster[0],hp,attack,defence,monster[4],monster[5],monster[6],monster[7],room)
	return m

def combat_view(charName,charMhp,charChp,charMmp,charCmp,monName,monMhp,monChp):
	print ("\n\n\n\n{}\t\t{}\nhp: {}/{}\t\thp: {}\nmp: {}/{}".format(charName,
	monName,charChp,charMhp,monChp,monMhp,charCmp,charMmp))

def combat(character,monster):
	