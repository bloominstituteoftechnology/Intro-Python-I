# FAQ

<!-- TODO
positional args vs keyword ards
What's the difference between inheritance and polymorphism?
-->

## Contents

### General CS

* [What are some things we can do to prepare for CS?](#q100)
* [What are some ways to learn a new language?](#q3600)
* [Why test code frequently?](#q3700)
* [Why isn't official documentation more helpful than Stack Overflow?](#q3800)
* [During an interview, what do I do if I can't remember the exact syntax?](#q3900)

### General Python

* [In regard to the code challenge solution, why is the '+' operator being used to concatenate strings? I thought we were supposed to use the join() method in Python?](#q300)
* [How do you get out of the Python built-in `help`?](#q400)
* [Are there any helpful VS Code extensions that are recommend for using with Python?](#q500)
* [I'm on Windows; what command do I use to run Python?](#q600)
* [What version of Python do I need?](#q700)
* [How do I get out of the Python REPL?](#q900)
* [What does "REPL" mean?](#q1000)
* [I'm on a Mac and when I run Python it says I'm on version 2.7. Why?](#q1100)
* [Does Python use tabs or spaces?](#q1200)
* [Can you use boolean shortcut assignments?](#q1700)
* [Can you do anonymous functions?](#q1800)
* [What are all those method names with double underscores around them?](#q2000)
* [Where are good Python docs?](#q2600)
* [Which linter?](#q2700)
* [What's the difference between __repr__ and __str__?](#q3300)
* [How does `sys.argv` work?](#q3400)

### Pipenv

* [Do I need to use pipenv?](#q800)
* [When do we run pipenv shell?](#q2200)
* [How do I get out of the pipenv shell?](#q2300)
* [How do I install additional packages from pipenv?](#q2400)
* [Is it possible to use system-wide packages from inside the virtual environment?](#q2500)

### Object-Oriented Programming

* [Why is there such a debate between OOP and functional programming, and why should we care?](#q200)
* [Following this flow: 1) class Dog is created with attributes size and weight. 2) New instance called Snoopy of class Dog is created. 3) Class Dog gets the method bark() dynamically added to it. Question: will Snoopy now have access to bark() method?](#q2900)
* [Can you dynamically add new methods/properties to class through other functions? Or must all properties/methods be declared at once?](#q2800)
* [If a subclass inherits from two superclasses with a method of the same name, which method will the subclass use?](#q3000)
* [How to handle multiple inheritance and why/when to do it in the first place?](#q3100)

### Python Scoping

* [Does Python have hoisting?](#q1400)
* [Does scoping work similar to other languages?](#q1500)
* [Can you return a reference to a function from another function? Or store it in a variable?](#q1600)
* [Can you do anonymous functions?](#q1800)

### Types

* [How do I convert an iterator into a list?](#q1300)
* [Is a dict like a JavaScript object?](#q1900)
* [How do I get a value from a dict?](#q2100)
* [Why use tuples instead of lists?](#q3200)
* [How do I concatenate two arrays into a single array?](#q3500)

## Questions

<a name="q100"></a>
### What are some things we can do to prepare for CS?

* [CS Wiki](https://github.com/LambdaSchool/CS-Wiki/wiki)
* [Polya's Problem Solving Techniques](https://github.com/LambdaSchool/CS-Wiki/wiki/Polya%27s-Problem-Solving-Techniques)
* [Solving Programming Problems](https://github.com/LambdaSchool/CS-Wiki/wiki/Solving-Programming-Problems)
* [CS Reading List](https://github.com/LambdaSchool/CS-Wiki/wiki/Computer-Science-Reading-List)
* [How to Google effectively](https://github.com/LambdaSchool/CS-Wiki/wiki/How-to-Google-Effectively)
* [How to read specs and code](https://github.com/LambdaSchool/CS-Wiki/wiki/How-to-Read-Specifications-and-Code)
* [Command line primer](https://github.com/LambdaSchool/CS-Wiki/wiki/Command-Line-Primer)
* [Coding style guidelines](https://github.com/LambdaSchool/CS-Wiki/wiki/CS-Coding-Style-Guidelines)

------------------------------------------------------------------------

<a name="q200"></a>
### Why is there such a debate between OOP and functional programming, and why should we care?

There are a lot of [programming
paradigms](https://en.wikipedia.org/wiki/Programming_paradigm) and they all have
their strengths and weaknesses when it comes to solving different types of
problems.

People can be quite opinionated about their favorites, but it's important to
remember that no one language or paradigm is the right tool for all jobs. And,
additionally, that virtually all problems can be solved in any of the
declarative or imperative paradigms. (Some might produce cleaner, more elegant
code for a particular problem.)

Paradigms are the hardest thing to learn because you often have to take all the
knowledge you have about solving a problem in another paradigm and throw it out
the window. You have to learn new patterns and techniques to be effective.

But we encourage this kind of learning because most popular languages are to
some degree _multi-paradigm_, and the more techniques you know from more
paradigms, the more effective you are in that multi-paradigm langage.

------------------------------------------------------------------------

<a name="q300"></a>
### In regard to the code challenge solution, why is the '+' operator being used to concatenate strings? I thought we were supposed to use the join() method in Python? 

Using `join()` to join large numbers of strings is definitely faster in Python
than using the `+` operator to do it. The reason is that every time you `join()`
or use the `+` operator, a new string is created. So if you only have to
`join()` once, versus using `+` hundreds of times, you'll run faster.

That said, if you want to use the `join()` approach, you'll have to have all
your strings in a list, which uses more memory than just having the two or three
that you need at a time to use `+`. So there's a tradeoff.

Another tradeoff might be in readability. It might be easier to read the `+`
version. That's worth something.

Finally, if `+` is fast enough for this case, it might not be worth the time to
bother with making a list of strings to `join()`.

* [Speed comparison with different ways of concatenating strings](https://waymoot.org/home/python_string/)

------------------------------------------------------------------------

<a name="q400"></a>
### How do you get out of the Python built-in `help`?

Hit `q` for "quit".

It's a common command in Unix "pagers" (programs that show documents a page at a
time).

------------------------------------------------------------------------

<a name="q500"></a>
### Are there any helpful VS Code extensions that are recommend for using with Python?

* [Official VS Code Python Extension](https://code.visualstudio.com/docs/languages/python)

------------------------------------------------------------------------

<a name="q600"></a>
### I'm on Windows; what command do I use to run Python?

If you're running in PowerShell or cmd, use:

```
py
```

If in bash, use `python` or `python3`.

------------------------------------------------------------------------

<a name="q700"></a>
### What version of Python do I need?

You should have version 3.7 or higher. Test with:

```shell
python --version
```

------------------------------------------------------------------------

<a name="q800"></a>
### Do I need to use pipenv?

You should. Good Python devs know how.

------------------------------------------------------------------------

<a name="q900"></a>
### How do I get out of the Python REPL?

Hit `CTRL-D`. This is the way End-Of-File is signified in Unix-likes.

------------------------------------------------------------------------

<a name="q1000"></a>
### What does "REPL" mean?

_Read, Evaluate, Print Loop_.

It reads your input, evaluates it, and prints the result. And loops.

------------------------------------------------------------------------

<a name="q1100"></a>
### I'm on a Mac and when I run Python it says I'm on version 2.7. Why?

Macs come with version 2.7 by default. You'll need to install version 3.

And preferable use `pipenv` after that.

------------------------------------------------------------------------

<a name="q1200"></a>
### Does Python use tabs or spaces?

[PEP 8](https://www.python.org/dev/peps/pep-0008/) says four spaces.

------------------------------------------------------------------------

<a name="q1300"></a>
### How do I convert an iterator into a list?

Cast it:

```python
list(range(5))
```

produces:

```python
[0, 1, 2, 3, 4]
```

------------------------------------------------------------------------

<a name="q1400"></a>
### Does Python have hoisting?

No.

* [What is hoisting?](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)

------------------------------------------------------------------------

<a name="q1500"></a>
### Does scoping work similar to other languages?

Generally, and also not really. Variables are either global or function-local.

Since there are no declarations, there's no block-level scope.

It is similar to `var` in JavaScript.

------------------------------------------------------------------------

<a name="q1600"></a>
### Can you return a reference to a function from another function? Or store it in a variable?

Yes. Functions are [first-class citizens](https://en.wikipedia.org/wiki/First-class_citizen).

------------------------------------------------------------------------

<a name="q1700"></a>
### Can you use boolean shortcut assignments?

Yes, you can. This is common in Perl and JavaScript, but it's not particularly [idiomatic](https://en.wikipedia.org/wiki/Programming_idiom) in Python.

```python
x = SomethingFalsey or 5
```

------------------------------------------------------------------------

<a name="q1800"></a>
### Can you do anonymous functions?

You can use `lambda` for simple functions:

```python
adder = lambda x, y: x + y

adder(4, 5)   # 9

do_some_math(4, 5, lambda x, y: y - x)
```

------------------------------------------------------------------------

<a name="q1900"></a>
### Is a dict like a JavaScript object?

Sort of.

The syntax is different, though. In Python you must use `[]` notation to access elements. And you must use `"` around the key names.

------------------------------------------------------------------------

<a name="q2000"></a>
### What are all those method names with double underscores around them?

Those are function you typically don't need to use, but can override or call if you wish.

Most commonly used are:

* `__init__()` is the constructor for objects
* `__str__()` returns a string representation of the object
* `__repr__()` returns a string representation of the object, for debugging

------------------------------------------------------------------------

<a name="q2100"></a>
### How do I get a value from a dict?

```python
d = {
    "a": 2,
    "b": 3
}

print(d["a"])
```

You don't use dot notation.

------------------------------------------------------------------------

<a name="q2200"></a>
### When do we run pipenv shell?

`pipenv shell` puts you into your work environment. When you're ready to work, or run the code, or install new dependencies, you should be in your pipenv shell.

------------------------------------------------------------------------

<a name="q2300"></a>
### How do I get out of the pipenv shell?

Type `exit`.

------------------------------------------------------------------------

<a name="q2400"></a>
### How do I install additional packages from pipenv?

```shell
pipenv install packagename
```

------------------------------------------------------------------------

<a name="q2500"></a>
### Is it possible to use system-wide packages from inside the virtual environment?

This is [not recommended](https://pipenv.readthedocs.io/en/latest/diagnose/#no-module-named-module-name).

------------------------------------------------------------------------

<a name="q2600"></a>
### Where are good Python docs?

* [Official documentation](https://docs.python.org/3/) tutorial and library reference.

The official docs might be hard to read at first, but you'll get used to them
quickly

------------------------------------------------------------------------

<a name="q2700"></a>
### Which linter?

Pylint or Flake8. The latter seems to be a bit more popular.

------------------------------------------------------------------------

<a name="q2800"></a>
### Can you dynamically add new methods/properties to class through other functions? Or must all properties/methods be declared at once?

You can add them dynamically at runtime, but you have to add them to the class itself:

```python
class Foo():
    pass

f = Foo()

Foo.x = 12  # Dynamically add property to class

f.x == 12 # True!

def a_method(self):
    print("Hi")

Foo.hi = a_method  # Dynamically add method to class

f.hi()   # Prints "Hi"
```

This is not a common thing to see in Python, however.

------------------------------------------------------------------------

<a name="q2900"></a>
### Following this flow: 1) class Dog is created with attributes size and weight. 2) New instance called Snoopy of class Dog is created. 3) Class Dog gets the method bark() dynamically added to it. Question: will Snoopy now have access to bark() method?

Yes.

------------------------------------------------------------------------

<a name="q3000"></a>
### If a subclass inherits from two superclasses with a method of the same name, which method will the subclass use?

The answer to this is twofold:

1. Lots of devs and shops frown on multiple inheritance, so maybe just don't do
   it.
   ([Discussion](https://softwareengineering.stackexchange.com/questions/218458/is-there-any-real-reason-multiple-inheritance-is-hated))

2. As for the order in which methods of the same name are resolved, check out
   the [MRO Algorithm](https://en.wikipedia.org/wiki/C3_linearization) which is
   what Python uses.


------------------------------------------------------------------------

<a name="q3100"></a>
### How to handle multiple inheritance and why/when to do it in the first place?

```python
class Base1:
    pass

class Base2:
    pass

class Derived(Base1, Base2):  # Multiple inheritance
    pass
```

Sometimes multiple inheritance can lead to elegant solutions when a subclass
needs attributes from multiple, otherwise-unrelated parent classes.

However, [a lot of people find it's not worth the
trouble](https://softwareengineering.stackexchange.com/questions/218458/is-there-any-real-reason-multiple-inheritance-is-hated))
and opt for other solutions, like composition.

------------------------------------------------------------------------

<a name="q3200"></a>
### Why use tuples instead of lists?

* Tuples are immutable. There's a school of thought that says bugs can be reduced if you make as many things immutable as you can.
* Tuples are faster than lists to access.
* Some tuples (containing primitive types), can be used as `dict` keys.

------------------------------------------------------------------------

<a name="q3300"></a>
### What's the difference between __repr__ and __str__?

Generally speaking, `__repr__` is the string a dev would want to see if they
dumped an object to the screen. `__str__` is the string a user would want to see
if the object were `print()`ed.

The output of `__repr__` should be _valid Python code that can reproduce the
object_.

```python
class Goat:
    def __init__(self, leg_count):
        self.leg_count = leg_count

    def __repr__(self):
        return f'Goat(leg_count={self.leg_count})'

    def __str__(self):
        return f'a goat with {self.leg_count} legs'
```

In action:

```python
>>> g = Goat(4)
>>> str(g)
'a goat with 4 legs'
>>> g
Goat(leg_count=4)
>>> Goat(leg_count=4)  # output of __repr__ makes a clone of that object!
Goat(leg_count=4)
```

------------------------------------------------------------------------

<a name="q3400"></a>
### How does `sys.argv` work?

It's a list that holds _command line arguments_. This is a way for a user to run
your program and specify different behavior from the command line.

Here's a small program that prints the command line arguments:

```python
import sys

for i in range(len(sys.argv)):
    print(f'Argument #{i} is: {sys.argv[i]}')
```

and here's some output, assuming you named the script `foo.py`:

```screen
$ python foo.py
Argument #0 is: foo.py
```

```screen
$ python foo.py antelope buffalo
Argument #0 is: foo.py
Argument #1 is: antelope
Argument #2 is: buffalo
```

Note that the 0th element in the list is the name of the program.

Here's another program that prints up to whatever number the user specifies:

```python
import sys

for i in range(int(sys.argv[1])):
    print(i+1)
```

Example runs:

```screen
$ python foo.py 2
1
2
```

```screen
$ python foo.py 4
1
2
3
4
```

------------------------------------------------------------------------

<a name="q3500"></a>
### How do I concatenate two arrays into a single array?

Use `extend()`.

```python
a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)

print(a)   # [ 1, 2, 3, 4, 5, 6 ]
```

------------------------------------------------------------------------

<a name="q3600"></a>
### What are some ways to learn a new language?

* Figure out how variables and functions work.
* Build small toy programs to test individual features.
* Build a larger project that exercises many features.
* Don't get frustrated! Treat the problem like a curiosity, a thing to be studied.
* Do small tutorials or code-alongs.
* Find docs you like.
* Learn the differences between this language and one you know.
* Learn this language's way of doing the things you know.

Things to look for in the new language:

* Collections (arrays, vectors, dictionaries)
* Data types
* Iterators
* Flow control (if, while, loops, etc)
* Functions
* etc.

------------------------------------------------------------------------

<a name="q3700"></a>
### Why test code frequently?

It's often better to make progress in small increments than to write a bunch of
stuff and test it in one go.

Also, it's easier to stay motivated if you spend 10 minutes getting a first
version going, even if it's missing 99% of its features, and then starting to
iterate on that.

------------------------------------------------------------------------

<a name="q3800"></a>
### Why isn't official documentation more helpful than Stack Overflow?

Often official documentation is more geared toward being a concise reference.
Stack Overflow is more of an example-based learning environment.

Sometimes you need to know the specific details. In those cases, you can dig
into the spec, with all it's lawyerly language, and try to decipher what it is
you have to do.

Other times, you just need a getting-started example, and Stack Overflow is
great for that.

Both types of documentation have their purpose.

------------------------------------------------------------------------

<a name="q3900"></a>
### During an interview, what do I do if I can't remember the exact syntax?

Just say so.

"I can't remember how to add an element to the end of the list in Python... is
it `push()`? In any case, we'll call the function here that does that."

(Turns out it's `append()` in Python, but being honest and describing what it is
your're trying to do will get you 99% of the way there in an interview.)
