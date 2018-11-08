from room import Room
from data import *
from helpers import char_creator,Monster_Creator
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

p = char_creator(pn) #see helpers
	
print(p)

# m = Monster_Creator(goblin,r0)	format to make a monster	
# m.talk()							format to make a monster talk
# print(m.enter)					format for entering
# print(m.death)					format for exiting

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
		print (help) # help menu is in data
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

