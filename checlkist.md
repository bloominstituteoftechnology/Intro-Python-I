## Install and Environment Setup
- [ ] Python 3 Installed
- [ ] Pipenv Installed

## Day (1)
- [ ] `hello` -- Hello world
- [ ] `bignum` -- Print some big numbers
- [ ] `datatypes` -- Experiment with type conversion
- [ ] `modules` -- Learn to import from modules
- [ ] `printf` -- Formatted print output
- [ ] `lists` -- Python's version of arrays
- [ ] `slice` -- Accessing parts of lists
- [ ] `comp` -- List comprehensions
- [ ] `dicts` -- Dictionaries
- [ ] `func` -- Functions
- [ ] `fileio` -- Read and write from files
- [ ] `cal` -- Experiment with module imports
- [ ] `obj` -- Classes and objects

## Day (2) A simple text adventure!
- [ ] Put the Room class in room.py based on what you see in `adv.py`.
- [ ] Put the Player class in `player.py`.
- [ ] Follow the instructions `adv.py`.
- [ ] Figure out what all those `.pyc` files are.
* A *.pyc file is created for imported modules, and they are placed in the same directory containing the .py file. But a *.pyc file is never created for the main script for your program.
- [ ] Add more rooms.

## Day (3) 
- [ ] Add an Item class in a file item.py.
- [ ] Add capability to add items to rooms.
- [ ] Add capability to add Items to the player's inventory. 
- [ ] Add a new type of sentence the parser can understand: two words.
- [ ] Implement support for the verb get followed by an Item name. This will be used to pick up Items.
- [ ] Add functionality to allow the Player to `drop sword`, that will move it out of the player's inventory into the current room the player is in.
- [ ] Add the i and inventory commands that both show a list of items currently carried by the player.

## Day (4)
- [ ] Add a score to your Player class. Set it to 0.
- [ ] Add a single word command, score, that the user can type in to see their current score.
- [ ] Add a subclass to Item called Treasure. (Description, Value)
- [ ] Add an on_take method to Item.
- [ ] Override on_take in Treasure so that the player gets the value of the Treasure added to their score attribute but only the first time the treasure is picked up.
- [ ] Add an on_drop method to Item. Implement it similar to on_take.
- [ ] Add a subclass to Item called LightSource
- [ ] During world creation, add a lamp LightSource to a convenient Room
- [ ] Override on_drop in LightSource that tells the player "It's not wise to drop your source of light!" if the player drops it. (But still lets them drop it.)
- [ ] Add an attribute to Room called is_light that is True if the Room is naturally illuminated, or False if a LightSource is required to see what is in the room.
- [ ] Modify the main loop to test if there is light in the Room (i.e. if is_light is True or there is a LightSource item in the - [ ] Room's contents or if there is a LightSource item in the Player's contents).
- [ ] Modify the get/take code to print "Good luck finding that in the dark!" if the user tries to pick up an Item in the dark.