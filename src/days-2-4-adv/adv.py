from room import Room
from gameObjects import Player, Monster
from data import *
import random

n = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
r0 = Room(start)
r1 = Room(branch)
RL = [r0.name,r1.name]
rc = r0
while True:
	pName = input("welcome adventurer! What is your name?\n\n> ")
	if len(pName) > 0:
		break


pn = pName

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
			break
	else:
		print("\nsorry, did you misspell that?\n")

		
print(p)


#print (dir)
#print (place)
#print (visible)
##########################
###MAIN GAME LOOP BELOW###
##########################(needs work but still, that's where it is)
while True:
	print(n)
	print (rc)
	(dir,place,visible)=(zip(*rc.links))
	t = input("Enter a command, h for help, or q to quit: ")
	if t in dir:
		print('working')
	elif t == "h":
		print ("""Help:
w, a, s, and d are the primary direction keys.

You can press i to access your invientory.

currently from this room you can go to:
	""")
		for i in range(len(visible)):
			if(str(str(visible).split(',')[i][2:3:]) == 'v'):
				print ('{}, {}'.format(dir[i],place[i]))
				#only displays non-hidden options
	elif t == "q":
		print ('thanks for playing!')
		break
	elif t == "w" or t=="a" or t=="s" or t=="d":
		print('you can\'t go that way!')
	else:
		print("is that even a direction?")

