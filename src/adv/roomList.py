from room import Room
from item import Item
import itemList
import npclist

# Declare all the rooms
rooms = {
    'field': Room(
        "Field", "The wind blows through the fog covered field.  *CLOP* *CLOP* You... ride... with your trusty servant, Patsy.  You can see a castle looming to the North."
    ),
    
    'castleWall': Room(
        "The Castle Wall",
        "'HALT!  Who goes there?'  A voice challenges from atop the wall.  You look up and answer, 'It is I, Arthur, son of Uther Pendragon, from the castle of Camelot.  King of the Britons, defeator of the Saxons, sovereign of all England!'\n'Pull the other one!' he challenges again.\n'I am,' you say, 'And this is my servant Patsy.  We have ridden the length and breadth of the land in search of knights who will join me in my court at Camelot.  I must speak with your lord and master.'\n'What, ridden on a horse?' he asks.\n'Yes!' You respond.\n'You're USING coconuts!'",
        "The guards are now discussing back and forth.  'It could be carried by an African swallow!'\n'Oh, yeah, an African swallow maybe, but not a European swallow, that's my point.'\n'Oh, yeah, I agree with that...'\n'But then of course African swallows are not migratory.'\n'Oh, yeah...'\n'So they couldn't bring a coconut back anyway...'\nYou ride off.  *CLOP* *CLOP*\n\nTo the West lies a village.\nTo the East is a forest."
    ),

    'dennis': Room(
        "On the Road",
        'Along the road here, you get into a nice little chat with the local populace about forms of government.\n"Listen -- strange women lying in ponds distributing swords is no basis for a system of government.  Supreme executive power derives from a mandate from teh masses, not from some farcical aquatic ceremony.  You can\'t expect to wield supreme executive power just \'cause some watery tart threw a sword at you!"  \nThe road here bends, one end headed East, the other end headed North.'
    ),

    'plagueTown': Room(
        "Plague Town",
        '"Bring out your dead!" *CLANG* "Bring out your dead! *CLANG*  The road North is blocked by all the dead, and the Mortician is demanding payment.  The only road out is the one you came in from, to the South.',
        'The dead have been brought out.  You may go North to Camelot, or South along the road.',
    ),

    'bridgeCrossing': Room(
        "Bridge Crossing",
        "As you ride through the woods, you arrive at a bridge.  Two knights, one green, one black, battle fiercely before it.  After some time, the black knight runs the green knight through the visor of his helmet, and stands victorious.  You approach, looking to recruit this warrior.\n'You fight with the strength of many men, Sir knight.  I am Arthur, King of the Britons. ... I seek the finest and the bravest knights in the land to join me in my Court of Camelot.'\nHe does not respond.  You move to pass with Patsy.  'Come Patsy.'\n'NONE shall pass.' he says.\n'I have no quarrel with you, good Sir knight, but I must cross this bridge.'\n'Then you shall die.'",
        "After an epic battle, the Black Knight has called it a draw.  You are allowed to pass.  The trail through the forest runs West and East.  To the West looms a castle.  To the East is a village."
    ),

    'witchVillage': Room(
        'Witch on Trial',
        'You come up on the town during a very public trial.  The crowd is cheering to "BURN HER!"  Wiser heads prevail, however.\n"Quiet, quiet.  Quiet! There are ways of telling whether she is a witch.  Tell me, what do you do with witches?"  Cheers of "Burn!"  "And what do you burn apart from witches?" "Wood!" "So why do witches burn?"  It takes them a bit, but one of the brighter ones finally understands.  "B--...\'cause they\'re made of wood...?"  "Good!" The knight says, and continues.  "So how do we tell whether she is made of wood?  Does wood sink in water?"  All of them know better than that.  "What also floats in water?"  The crowd is stumped, but your mind is sharper than that, and you know the answer.  "A duck."  Now, all Bedemir needs, is a duck!  The only road in and out of town heads West.',
        'Now that the horrible witch has been taken care of, and you have knighted Sir Bedemir, you are sure this village is now much better off.  The only road in and out of town heads West.'
    ),

    'camelot': Room(
       '"Look, my liege!"  "Camelot!"  "Camelot!"  "Camelot!"  "It\'s only a model."  "Shhh!  Knights, I bid you welcome to your new home.  Let us ride... to Camelot!"',
       '',
   ),

   'god': Room(
       '',
       '',
   ),

   'france': Room(
       '',
       '',
   ),

   'threeHeads': Room(
       '',
       '',
   ),

   'castleAnthrax': Room(
       '',
       '',
   ),

   'enchanter': Room(
       '',
       '',
   ),

   'nee': Room(
       '',
       '',
   ),


#    '': Room(
#        '',
#        '',
#    ),
}


# Link rooms together
rooms['field'].n_to = rooms['castleWall']

rooms['castleWall'].s_to = rooms['field']
rooms['castleWall'].block_w_to = rooms['dennis']
rooms['castleWall'].block_e_to = rooms['bridgeCrossing']

rooms['dennis'].n_to = rooms['plagueTown']
rooms['dennis'].e_to = rooms['castleWall']

rooms['plagueTown'].block_n_to = rooms['camelot']
rooms['plagueTown'].s_to = rooms['dennis']

rooms['bridgeCrossing'].block_e_to = rooms['witchVillage']
rooms['bridgeCrossing'].w_to = rooms['castleWall']

rooms['witchVillage'].w_to = rooms['bridgeCrossing']




# Beginning world items
rooms['field'].roomInv = [itemList.spam1, itemList.stick]
rooms['castleWall'].roomInv = [itemList.rock, itemList.duck]
rooms['dennis'].roomInv = [itemList.spam2, itemList.shield]
rooms['plagueTown'].roomInv = [itemList.wagon, itemList.deadPerson, itemList.deadPerson, itemList.deadPerson, itemList.deadPerson]
rooms['bridgeCrossing'].roomInv = [itemList.deed, itemList.coin]
rooms['witchVillage'].roomInv = [itemList.spam3, itemList.ninePence]
#camelot
#god
#france
#threeHeads
#castleAnthrax
#enchanter
#nee


# Mobs and NPCs assigned to rooms
rooms['field'].npc = [npclist.ralph]
rooms['castleWall'].mobs = [npclist.guard1, npclist.guard2]
rooms['dennis'].npc = [npclist.dennis]
rooms['plagueTown'].npc = [npclist.deadPerson]
rooms['plagueTown'].mobs = [npclist.mortician]
rooms['bridgeCrossing'].mobs = [npclist.blackKnight]
rooms['witchVillage'].npc = [npclist.bedemir]
#camelot
#god
#france
#threeHeads
#castleAnthrax
#enchanter
#nee

# Required items assigned to rooms
#field
rooms['castleWall'].itemRequired = [itemList.coconuts]
#dennis
rooms['plagueTown'].itemRequired = [itemList.ninePence]
rooms['bridgeCrossing'].itemRequired = [itemList.excaliber]
rooms['witchVillage'].itemRequired = [itemList.duck]
#camelot
#god
#france
#threeHeads
#castleAnthrax
#enchanter
#nee


##ROOM LIST##
#field
#castleWall
#dennis
#plagueTown
#bridgeCrossing
#witchVillage
#camelot
#god
#france
#threeHeads
#castleAnthrax
#enchanter
#nee
