from room import Room
from player import Player

# Declare all the rooms

room = {
    'cell_1':  Room("The Orange Room",
                     """You wake up on a cold, metal floor, your head pounding, your body freezing.
You take a few deep, cold breaths, rubbing the sides of your head, willing the pain to go away.
It finally recedes enough for you to look around and get your bearings.  You find yourself in some 
sort of cell with a orange ambient light emitting from nothing.  Screams reverberate somewhere far away
through the metal.  Visions of sex, drugs, drink, orgies, parties, wild abandon, all fill your head.
You shake it away.  You are in some sort of metal box, about twelve feet per side.  As you stand, a
voice speaks from nowhere.\n
\t\"Hear the screaming?  Are you not better than them?  You do not belong here.  They
are filthy.  They are disgusting, and putrid.  Think of all that they have done.\"\n
You jump, and look around for the owner of the voice, but see no one.  Taking a closer look
at your surroundings, you see something written on one of the walls.  Confused and dazed, you slowly
stumble over to it, to see what it says.
\n
\t\"1. Success is getting what you want.  Happiness is wanting what you get.\"
\t\"2. This too shall pass.\"
\t\"3. For all have sinned, and come short of the glory of God.\"
\nChoose Honestly."""),

    'cell_2':  Room("The Red Room",
                    """You blink.  Your world spins, and you feel like you are falling through space, head over heels.
A voice whispers in your mind.
"Blessed are they whose iniquities are forgiven, and whose sins are covered."
\nYou blink.  You are in another room.
This room is lit red from some unknown source.  It smells of sweat, sex, perfume, and cigarette smoke.
Your nose wrinkles at the sudden change of scent, but you also find yourself strangely aroused.  The room
is no longer metal, but seems to be dark glass.  The images from the previous room stumble through your brain.
A seductive voice whispers behind you.
\"You made it.  Now claim your reward.\"
You jump at the voice, spinning around, to find nothing there.  But on the wall ahead, is more writing.
\n
\t\"1. If it feels good, do it.\"
\t\"2. Marriage is honourable in all, and the bed undefiled.\"
\t\"3. God wants me to be happy.\"
\nChoose Honorably."""),

    'cell_3':  Room("The Green Room",
                    """You blink.  You are falling again.  You can hear people yelling.  You listen closer.
\"Master, this woman was taken in adultery, in the very act!  Moses in the law commanded us, that such
people should be stoned: but what do you say?\"
You can hear shuffling, people mumbling.  It's quiet for a moment.  Then the voices start again, accusing
whoever this woman is, asking what is to be done with her.  Then, a solitary voice responds, as if right
beside you.
\"Whoever among you that has no sin, throw the first stone at her.\"
The voices grow quiet, and stop.  There is shuffling moving away, and lasts for a while.  Then silence.
You can hear a woman crying.
After some time, the solitary voice speaks again.
"Woman, where are your accusers?  Who condemns you?"
In a voice broken with sobs, the woman responds, "No one, Lord..."
"Neither do I condemn you.  Go, and sin no more."
\nYou blink.  You are in another room.
This room is lit green, and smells of alcohol, cigars, and the musty stink of dollar bills.
You can hear the faint tinkling of coins and the flapping of money counters.
This room is made of smooth, polished wood, the grains weaving a complex pattern on the walls.
You know what you're supposed to do.  You look around, and find the words written on the wall.
\n
\t\"1. Money cometh to me now!\"
\t\"2. God helps those who help themselves.\"
\t\"3. For where your treasure is, there will your heart be also.\"
\nChoose Eternally"""),

    'cell_4':  Room("The Blue Room",
                    """You blink.  As you're falling, that solitary voice from before speaks as if from some distance.
\"Lay not up for yourselves treasures upon earth, where moth and rust currupt, and where thieves break in
and steal.  But lay up for yourselves treasures in heaven, where neither moth nor rust corrupt, and where
thieves do not break in nor steal.  For where your treasure is, there will your heart be also.\"
\nYou blink.  Another room.  This one is blue, and feels pleasantly warm.  The walls are simple, regular,
house walls.  They're painted a light blue, and the plush, blue carpet beneath your feet feels quite wonderful.
It smells of fresh linen, and baking cookies.
\"God just wants us to love.\"
You stand there, confused.  Isn't this voice supposed to say something wrong?  Shaking your head, you approach
the writing on the wall.
\n
\t\"1. He that loves father or mother... son or daughter more than me is not worthy of me.\"
\t\"2. All, everything that I understand, I only understand because I love.\"
\t\"3. Love is blind.\"
\nChoose Humbly"""),

    'cell_5':  Room("The White Room",
                    """You blink.  Falling.  Again.  This time, the voice is different.  It's...  two people talking.
The first voice is the solitary voice from before, but echoing his voice is another, following only
a moment after the first, as if copying what the solitary voice speaks.  This other voice is older, as if the man
speaking is older, more feeble.  Time has passed for this voice.  But it speaks with authority, as it echoes the first,
as if it finds its strength in the first voice.
\"And then shall that wicked one be revealed, whom the Lord shall consume with the spirit of his mouth, and shall destroy
with the brightness of his coming: Even him, whose coming is after the working of Satan with all power and signs and
lying wonders, and with all deceivableness of unrighteousness in them that perish; because they received not the love of
the truth, that they might be saved.  And for this cause God shall send them strong delusion, that they should believe a
lie: That they all might be damned who believed not the truth, but had pleasure in unrighteousness.\"
\nYou blink.  The meaning of the words hit home as you stand up in a white room.  You cannot make sense of the shape of the
room.  There is no shadow, only light.  Only one spot stands out in stark contrast to the rest of the room.  Words, on the
wall, written in red.
\n
\t\"1. ... your eyes shall be opened, and ye shall be as gods, knowing good and evil.\"
\t\"2. All these things will I give thee, if thou wilt fall down and worship me.\"
\t\"3. In whom we have redemption through his blood, the forgiveness of sins, according to the riches of his grace.\"
\nChoose Rightly"""),

    'finish':  Room("Awaken",
                    """You blink.  You are not falling.  You are...  held.  Something... or someone... holds you.
As if in the palm of their hand.  You can feel the power of the being holding you.  Terrifyingly
powerful, yet...  calming.  At any moment, that hand could drop you into eternity, damned, yet
you can feel the love that holds you there, paitiently, waiting for a decision.
\nThat solitary voice speaks to your heart one last time.
\"I am the way, the truth, and the life: no man cometh unto the Father but by me.\"
\n
\t\"1. Ignore Him.\"
\t\"2. Seek Him.\"
\nChoose Wisely"""),

    'thankYou':  Room("Thank You",
                    """Thank you for playing my little game.  I hope that you got out of it at least as much as I put into it.
My purpose for this game was to try and instill a desire to know the Truth of the Word of God.
There are many misconceptions out there, and many people that believe in the Bible, but have not read it for themselves.
If you are one of these many, I hope that this game has caused a desire to seek the Truth of the Word.
If you would like help in searching the Scriptures, I suggest this free program:
\nThru The Bible with Dr. J. Vernon McGee
http://www.ttb.org/programs/the-5-year-study

Please enter Q to quit.
"""),

    'hell': Room("Game Over", """As soon as you choose the words, your world turns black, and
malevolent laughter pours over your soul.
\n"You will join me, FOREVER!\"
\n\nAfter all, \"Misery loves company\" ... right?\n
... RIGHT?!?!"""),

    'roomName': Room("Room Name", """Description"""),
}


# Link rooms together

room['cell_1'].one = room['hell']
room['cell_1'].two = room['hell']
room['cell_1'].three = room['cell_2']

room['cell_2'].one = room['hell']
room['cell_2'].two = room['cell_3']
room['cell_2'].three = room['hell']

room['cell_3'].one = room['hell']
room['cell_3'].two = room['hell']
room['cell_3'].three = room['cell_4']

room['cell_4'].one = room['cell_5']
room['cell_4'].two = room['hell']
room['cell_4'].three = room['hell']

room['cell_5'].one = room['hell']
room['cell_5'].two = room['hell']
room['cell_5'].three = room['finish']

room['finish'].one = room['thankYou']
room['finish'].two = room['thankYou']

# room[''].one = room['']
# room[''].two = room['']
# room[''].three = room['']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room["cell_1"], 10)
playing = True

# Write a loop that:
while playing is True:
# * Prints the current room name
    print('\n%s\n' % (player.location.name))
# * Prints the current description (the textwrap module might be useful here).
    print(player.location.description)
# * Waits for user input and decides what to do.
    direction = str(input('\n\nWhat do you say? 1, 2, or 3? (Q to quit):'))
    print('\n____________________________________________\n')
#
# If the user enters a cardinal direction, attempt to move to the room there.
    try:
        if direction == '1':
            player.location = player.location.one
        elif direction == '2':
            player.location = player.location.two
        elif direction == '3':
            player.location = player.location.three
        elif direction == 'q' or direction == 'Q':
            break
    except:
        raise ValueError("That is not an option.")
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
