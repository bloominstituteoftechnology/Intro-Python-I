# ROOMS

start = ["cheesy beginnings","the room smells strongly of... cheese? There is a passage to the north.",
["w","p"],["a split in the road","hidden room"],["v","h"]]

branch = ["a split in the road","""travelling further, the road splits off.
To the left, a forest, and to the right, some open plains""",
["a","d", "s"],["forest","plains","cheesy beginnings" ],["v","v","v"]]

# ROOMS

# DROP TABLES

c1 = ["dagger","old coin","dented helmet"]
c2 = ["tea cup","short sword","dusty tome"]
c3 = ["leather boots","purple powder","odd rock"]
c4 = ["rusty chainmail","health potion","mana potion"]
c5 = ["buckler","silk","berries"]
c6 = ["staff","blacksmith's hammer","worn-out robe"]

uc1 = ["longsword","kiteshield","salt rocks"]
uc2 = ["wand of fire","platemail","strong healing potion"]
uc3 = ["viking helmet","strong mana potion","obsidian dagger"]

r1 = ["sword of the oceans","life-essance potion","cloak of shadows"]

# DROP TABLES

# MONSTERS

# MONSTER LINES

gobl = ["Oh look, free exp, I mean... A goblin!","The goblin tries to run away, but then realizes it isn't programmed to do that."
,"The goblin casts M E T E O R\n... Just kidding, it's still a weak goblin."]

ogrl = ["\'WHAT ARE YOU DOING IN MY SWAMP\' the mighty ogre bellows","You wonder why you're fighting sometyhing as strong as an ogre",
"Is the loot even worth it? Depends if you're willing to risk death"]

# MONSTERS

goblin = ["goblin",6,2,1,gobl,"A goblin attacks you!","You have slain the MIGHTY POWERFUL goblin!",[c1,c3,c5]]
ogre = ["ogre",15,3,1,ogrl,"An OGRE is standing in the way!","The fight is finally... Ogre.",[c6,uc2,uc3]]


# MONSTERS