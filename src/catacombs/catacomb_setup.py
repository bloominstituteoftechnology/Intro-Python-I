from room import Room
from item import Item, Treasure, LightSource

commandsHelp = {
"n" : "Go North",
"w" : "Go West",
"e" : "Go East",
"s" : "Go South",
"l" : "Look",
"i" : "Inventory",
"p" : "Pickup",
"u" : "Use",
"d" : "Drop",
"a" : "Attack",
"score" : "Score",
"q" : "Quit",
"h" : "help",
}

#set light sources
# room["foyer"].isLit = False
#declare all items
item = {
   "coin" : Treasure("Coin", "A shiny golden coin"),
   "scepter": Treasure("Scepter", "A short silver staff with a huge sapphire inlaid on top", 1000),
   "necklace" : Treasure("Necklace", "A heavy gold necklace set with 3 large diamonds surrounded by smaller rubies", 500),
   "torch" : LightSource("Torch", "An excellent source of light")
}
# room["foyer"].inventory["coin"] = item["coin"]
# room["treasure"].inventory["scepter"] = item["scepter"]
# room["overlook"].inventory["necklace"] = item["necklace"]
# room["outside"].inventory["torch"] = item["torch"]

###############################################
roomNames = ["exit", "start", "TreasureRoom"]
roomDescriptions = {
"You feel crunching underneath your feet and look down to see the floor littered with bones",
"As you enter the room, a cold chill runs down your spine. This place gives you the creeps.",
"Rats everywhere, squeaking madly as they run over your feet. What are they running from?",
"You brush cobwebs out of your face and peer around the dim room. It seems empty.",
"""Broken barrels are strewn about the floor in front of you. 
This was a storage room of some kind, though nearly everything is long gone now. """,
"You squeeze through a broken door to find yourself in a cramped hallway.",
"""Skulls line the walls and a large stone casket sits in the center of the room. 
It's cover lies broken on the floor. You peer inside and see frantic scratches everywhere, but no corpse.""",
"""You push through a heavy stone door and enter a large room.
Stone shelves are set in every wall, each shelf full of stone urns.""",
"""A foul smell hits your nostrils as you enter an antechamber.
The floor is covered in a sticky, black substance. You quickly scramble around,
searching for a way out of this terrible place.""",
"""What was once a large animal lays on the ground in front of you. 
Huge teeth marks cover its back as an impossibly big chunk appears missing.
The animal looks to have been here for quite some time.""",
"""You push your way into a cramped room, barely larger than a closet.
You stretch your arms out and touch both walls at the same time, but quickly recoil
 as a huge spider runs over your fingers.""",
"""You stumble and slam face first into the stone floor.
Cursing silently, you pick yourself off the ground.
Looking back to see what tripped you, you spot a large cow's skull.
One of it's horns seems to have been bitten clean off.""",
"Old stone walls, slick stone floor. You wonder if you will ever find a way out this maze.",
"""As you open the door, hundreds of bones pour out from the next room.
You scramble over them, trying your best to swim through and find an exit.""",
"""The walls are covered in old tapestries. It looks like they tell a story, though you cannot tell of what.
  The final tapestry depicts hundreds of people streaming out of a cavern.
  A huge boulder is being rolled to seal the cave shut. 
  The tapestry is dusty but you lean in and your eyes catch a glimpse of what may be 
  two terrible red eyes inside the blackness of the cavern.""",
 """Crunching under your feet causes you to look downward. 
 Thousands of bugs cover the floor around you, making it difficult to see the stone underneath.""",
 "Another empty room.",
 """A huge hole lies in the center of the room. You drop a rock down and wait for the sound of it hitting bottom.
 It doesn't.""",
 """You enter a large room filled with short benches. A huge stone pedestal sits in the center of the room. 
 An uneasy feeling sits in your stomach, and you long to be gone from this place.""",
 """Loud shrieks pierce your ears and warm furry creatures swarm your face.
 The bats pour out the door behind you as you thrash about until they are all gone.""",
 """The smell of sewage surrounds you as you quickly bring a hand to cover your nose. 
 Quickly you look for a way out of this foul room.""",
 "A large table sits in the center of the room. Wooden utensils lay strewn about the floor.",
 """As you enter the room, something skitters across the floor behind you.
  You whip your head around, but it disappeared.""",
}
exitDescription = """You hear a faint whistling and scramble around the room looking for its orign.
Your fingers find a thin crack between stones and you frantically push and kick against it with all your might.
The stones give way to reveal a wide open plain before you. Freedom."""
monsterStartRoom = """You open one of the huge double doors before you.
You enter a gigantic chamber, filled with thousands of bones. The whole room is covered with dust,
save for a large clearing in the center. A path of crushed and flattened bones goes directly from the clearing
stright to the doorway of you entered."""
startingDescription = """The room is cold and empty, covered in slick stone brick.
 A thick layer of dust covers every surface"""

monsters = {
    "Minotaur" : """A huge bipedal beast, standing over 10 feet tall on its cloven hooves.
    It's head is similar to that of a bull, with menacing horns stained black from use and a long snout.
    The fiend snarls at you, baring gigantic razor sharp teeth. It lunges toward you with large, human-like hands""",
    "Werewolf" : """A gigantic dog-like creature charges at you. It is larger than any dog or wolf you have ever seen,
    resembling a bear more than anything. As the creature closes the distance between you, it pushes off the ground 
    into an upright position, readying claws the size of daggers to rip you into pieces.""",
}