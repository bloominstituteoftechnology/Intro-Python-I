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

Learn the basics of Python with a pile of toy programs.

Take a look in the `src/` directory.

NOTE: `adv.py` is for Day 2, so ignore it for today.

Suggested order for implementing the toy programs:

* `hello` -- Hello world
* `bignum` -- Print some big numbers
* `datatypes` -- Experiment with type conversion
* `printf` -- Formatted print output
* `lists` -- Python's version of arrays
* `comp` -- List comprehensions
* `dicts` -- Dictionaries
* `func` -- Functions
* `cal` -- Experiment with module imports
* `obj` -- Classes and objects

## Day 2

Put it together into a bigger toy program: a simple text adventure!

This is in `src/adv.py`. Check it out!

Stretch goals:

* Add more rooms.

* Add things to the game that can be found in rooms, e.g. sword, lamp.
  The room can keep a list of things found within it.

* Show a listing of the things in room when the player walks into it.

* Add functionality to allow the user to `take sword`, that will move it
  out of the room and into a list on the player called `inventory`.

* Add the `i` command to show what is in the player's inventory.

* Add functionality to allow the user to `drop sword`, that will move it
  out of the player's inventory into the current room the player is in.

* Add a way to win.

* Come up with more stretch goals! Scoring? Monsters?
