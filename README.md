# Intro to Python

## Goals

It's time to learn a new language! Python!

Python is a popular, easy-to-use programming language that has significant
traction in the field.

Remember the goal is _learning to learn_, so keep track of what works for you
and what doesn't as you go through the process of exploring Python.

## Techniques for learning new languages

* Try to relate things you already know in another language (e.g. what an
  _array_ is) to the corresponding things in Python (e.g. a _list_) and how to
  use them.

* Write a bunch of "toy programs" that demonstrate different key features of the
  language

* Explore the standard library that's available for the language. Skim it
  briefly for now--the idea isn't to memorize everything but to file away
  generally what functionality is available.

* Write a more substantial toy program that uses a variety of the features.

Again, keep track of what works for you. Try different things to see what works
best for learning new languages.

## Resources

* [Installing Python and pipenv](https://github.com/LambdaSchool/CS-Wiki/wiki/Installing-Python-3-and-pipenv)
* [JavaScript<->Python cheatsheet](https://github.com/LambdaSchool/CS-Wiki/wiki/Javascript-Python-cheatsheet)
* [How to read Specs and Code](https://github.com/LambdaSchool/CS-Wiki/wiki/How-to-Read-Specifications-and-Code)
* [Python 3 standard library](https://docs.python.org/3.6/library/)

## Getting started

1. Make sure you have Python 3 and pipenv installed.

2. Go to the directory with the `Pipfile` and run
   ```
   pipenv install
   ```

3. After the install completes, run
   ```
   pipenv shell
   ```
   This will get you into the virtual environment. At this point, you should be
   able to run Python 3 by just running `python`:
   ```
   $ python --version
   Python 3.6.5
   ```

   You can exit the virtual environment by typing `exit`.

## Day 1

### Goals

* Learn the basic syntax and structure of Python

### Summary

* Implement a number of tiny Python programs that demonstrate Python syntax.

### Instructions

Take a look in the `src/` directory.

NOTE: `adv/` is for Day 2, so ignore it for today.

Suggested order for implementing the toy programs:

* `hello` -- Hello world
* `bignum` -- Print some big numbers
* `datatypes` -- Experiment with type conversion
* `modules` -- Learn to import from modules
* `printf` -- Formatted print output
* `lists` -- Python's version of arrays
* `tuples` -- Immutable lists typically for heterogenous data
* `slice` -- Accessing parts of lists
* `comp` -- List comprehensions
* `dicts` -- Dictionaries
* `func` -- Functions
* `args` -- Arguments and Keyword Arguments
* `scope` -- Global, Local, and Non-Local scope
* `fileio` -- Read and write from files
* `cal` -- Experiment with module imports
* `obj` -- Classes and objects

## Day 2

### Goals

* Solidify the Python basics


### Summary

* Implement a basic text adventure game
* Add classes for rooms and the player
* Add a simple parser that reads user input and performs actions

### Instructions

This is in `src/adv/`. Check it out!

* Put the Room class in room.py based on what you see in `adv.py`.

* Put the Player class in `player.py`.

* Follow the instructions `adv.py`.

* Figure out what all those `.pyc` files are that appear after you successfully
  run the program.

## Day 3

### Goals

* Prepare for more OOP techniques
* Practice classes and lists

### Summary

* Add items to the game that the user can carry around
* Make rooms able to hold multiple items
* Make the player able to carry multiple items
* Add two-word commands to the parser
* Add the `get` and `drop` commands to the parser

### Instructions

* Add an `Item` class in a file `item.py`.

  * This will be the _base class_ for specialized item types to be declared
    later.

  * The item should have `name` and `description` attributes.

     * Hint: the name should be one word for ease in parsing later.

* Add capability to add items to rooms.

  * The `Room` class should be extended with a `list` that holds the `Item`s
    that are currently in that room.

  * Add functionality to the main loop that prints out all the items that are
    visible to the player when they are in that room.

* Add capability to add `Item`s to the player's inventory. The inventory can
  also be a `list` of items "in" the player, similar to how `Item`s can be in a
  `Room`.

* Add a new type of sentence the parser can understand: two words.

  * Until now, the parser could just understand one sentence form:

     `verb`

    such as "n" or "q".

  * But now we want to add the form:

    `verb` `object`

    such as "take coins" or "drop sword".

  * Split the entered command and see if it has 1 or 2 words in it to determine
    if it's the first or second form.

* Implement support for the verb `get` followed by an `Item` name. This will be
  used to pick up `Item`s.

  * If the user enters `get` or `take` followed by an `Item` name, look at the
    contents of the current `Room` to see if the item is there.

     * If it is there, remove it from the `Room` contents, and add it to the
       `Player` contents.

     * If it's not there, print an error message telling the user so.

* Implement support for the verb `drop` followed by an `Item` name. This is the
  opposite of `get`/`take`.

* Add the `i` and `inventory` commands that both show a list of items currently
  carried by the player.

## Day 4

### Goals

* Practice inheritance
* Practice method overriding
* Be able to call superclass methods
* Implement a callback/event structure

### Summary

* Add scoring
* Subclass items into treasures
* Subclass items into light sources
* Add methods to notify items when they are picked up or dropped
* Add light and darkness to the game

### Instructions

* Add a `score` to your `Player` class. Set it to 0.

* Add a single word command, `score`, that the user can type in to see their
  current score.

* Add a subclass to `Item` called `Treasure`.

  * The `Treasure` constructor should accept a name, description, and value.

* During world creation, add three `Treasure`s to convenient `Room`s.

* Add an `on_take` method to `Item`. 

  * Call this method when the `Item` is picked up by the player.

  * The `Item` can use this to run additional code when it is picked up.

* Override `on_take` in `Treasure` so that the player gets the value of the
  `Treasure` added to their `score` attribute _but only the first time the
  treasure is picked up_.
  
  * If the treasure is dropped and picked up again later, the player should
    _not_ have the value added to their score again.

* Add an `on_drop` method to `Item`. Implement it similar to `on_take`.

* Add a subclass to `Item` called `LightSource`.

* During world creation, add a `lamp` `LightSource` to a convenient `Room`.

* Override `on_drop` in `LightSource` that tells the player "It's not wise to
  drop your source of light!" if the player drops it. (But still lets them drop
  it.)

* Add an attribute to `Room` called `is_light` that is `True` if the `Room` is
  naturally illuminated, or `False` if a `LightSource` is required to see what
  is in the room.

* Modify the main loop to test if there is light in the `Room` (i.e. if
  `is_light` is `True` **or** there is a `LightSource` item in the `Room`'s
  contents **or** if there is a `LightSource` item in the `Player`'s contents).

  * If there is light in the room, display name, description, and contents as
    normal.

  * If there isn't, print out "It's pitch black!" instead.

  * Hint: `isinstance` might help you figure out if there's a `LightSource`
    among all the nearby `Item`s.

* Modify the `get`/`take` code to print "Good luck finding that in the dark!" if
  the user tries to pick up an `Item` in the dark.

## Stretch Goals

In arbitrary order:

* Add more rooms.

* Add more items to the game.

* Add a way to win.

* Add more to the parser.

  * Remember the last `Item` mentioned and substitute that if the user types
    "it" later, e.g.

    ```
    take sword
    drop it
    ```

  * Add `Item`s with adjectives, like "rusty sword" and "silver sword".

    * Modify the parser to handle commands like "take rusty sword" as well as
      "take sword".

      * If the user is in a room that contains both the rusty sword _and_ silver
        sword, and they type "take sword", the parser should say, "I don't know
        which you mean: rusty sword or silver sword."

* Modify the code that calls `on_take` to check the return value. If `on_take`
  returns `False`, then don't continue picking up the object. (I.e. prevent the
  user from picking it up.)

  * This enables you to add logic to `on_take` to code things like "don't allow
    the user to pick up the dirt unless they're holding the shovel.

* Add monsters.

* Add the `attack` verb that allows you to specify a monster to attack.

* Add an `on_attack` method to the monster class.

* Similar to the `on_take` return value modification, above, have `on_attack`
  prevent the attack from succeeding unless the user possesses a `sword` item.

* Come up with more stretch goals! The sky's the limit!
