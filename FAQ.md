# FAQ

## General CS

<p><details><summary><b>What are some things we can do to prepare for CS?</b></summary><p>

* [CS Wiki](https://github.com/LambdaSchool/CS-Wiki/wiki)
* [Polya's Problem Solving Techniques](https://github.com/LambdaSchool/CS-Wiki/wiki/Polya%27s-Problem-Solving-Techniques)
* [Solving Programming Problems](https://github.com/LambdaSchool/CS-Wiki/wiki/Solving-Programming-Problems)
* [CS Reading List](https://github.com/LambdaSchool/CS-Wiki/wiki/Computer-Science-Reading-List)
* [How to Google effectively](https://github.com/LambdaSchool/CS-Wiki/wiki/How-to-Google-Effectively)
* [How to read specs and code](https://github.com/LambdaSchool/CS-Wiki/wiki/How-to-Read-Specifications-and-Code)
* [Command line primer](https://github.com/LambdaSchool/CS-Wiki/wiki/Command-Line-Primer)
* [Coding style guidelines](https://github.com/LambdaSchool/CS-Wiki/wiki/CS-Coding-Style-Guidelines)
</p></details></p>

<p><details><summary><b>Why is there such a debate between OOP and functional programming, and why should we care?</b></summary><p>

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

</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>In regard to the code challenge solution, why is the '+' operator being used to concatenate strings? I thought we were supposed to use the join() method in Python? </b></summary><p>

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
</p></details></p>

## Python

<!-- =============================================================================== -->

<p><details><summary><b>How do you get out of the Python built-in <tt>help</tt>?</b></summary><p>

Hit `q` for "quit".

It's a common command in Unix "pagers" (programs that show documents a page at a
time).

</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Are there any helpful VS Code extensions that are recommend for using with Python?</b></summary><p>

* [Official VS Code Python Extension](https://code.visualstudio.com/docs/languages/python)
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>I'm on Windows; what command do I use to run Python?</b></summary><p>

If you're running in PowerShell or cmd, use:

```
py
```

If in bash, use `python` or `python3`.
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>What version of Python do I need?</b></summary><p>

You should have version 3.7 or higher. Test with:

```shell
python --version
```
</p></details></p>


<!-- =============================================================================== -->

<p><details><summary><b>Do I need to use pipenv?</b></summary><p>

You should. Good Python devs know how.
</p></details></p>


<!-- =============================================================================== -->

<p><details><summary><b>How do I get out of the Python REPL?</b></summary><p>

Hit `CTRL-D`. This is the way End-Of-File is signified in Unix-likes.
</p></details></p>


<!-- =============================================================================== -->

<p><details><summary><b>What does "REPL" mean?</b></summary><p>

_Read, Evaluate, Print Loop_.

It reads your input, evaluates it, and prints the result. And loops.
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>I'm on a Mac and when I run Python it says I'm on version 2.7. Why?</b></summary><p>

Macs come with version 2.7 by default. You'll need to install version 3.

And preferable use `pipenv` after that.
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Does Python use tabs or spaces?</b></summary><p>

[PEP 8](https://www.python.org/dev/peps/pep-0008/) says four spaces.
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>How do I convert an iterator into a list?</b></summary><p>

Cast it:

```python
list(range(5))
```

produces:

```python
[0, 1, 2, 3, 4]
```
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Does Python have hoisting?</b></summary><p>

No.

[What is hoisting?](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Does scoping work similar to other languages?</b></summary><p>

Generally, and also not really. Variables are either global or function-local.

Since there are no declarations, there's no block-level scope.

It is similar to `var` in JavaScript.
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Can you return a reference to a function from another function? Or store it in a variable?</b></summary><p>

Yes. Functions are [first-class citizens](https://en.wikipedia.org/wiki/First-class_citizen).
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Can you use boolean shortcut assignments?</b></summary><p>

Yes, you can. This is common in Perl and JavaScript, but it's not particularly [idiomatic](https://en.wikipedia.org/wiki/Programming_idiom) in Python.

```python
x = SomethingFalsey or 5
```
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Can you do anonymous functions?</b></summary><p>

You can use `lambda` for simple functions:

```python
adder = lambda x, y: x + y

adder(4, 5)   # 9

do_some_math(4, 5, lambda x, y: y - x)
```
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Is a dict like a JavaScript object?</b></summary><p>

Sort of.

The syntax is different, though. In Python you must use `[]` notation to access elements. And you must use `"` around the key names.
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>What are all those method names with double underscores around them?</b></summary><p>

Those are function you typically don't need to use, but can override or call if you wish.

Most commonly used are:

* `__init__()` is the constructor for objects
* `__str__()` returns a string representation of the object
* `__repr__()` returns a string representation of the object, for debugging
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>How do I get a value from a dict?</b></summary><p>

```python
d = {
    "a": 2,
    "b": 3
}

print(d["a"])
```

You don't use dot notation.
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>When do we run pipenv shell?</b></summary><p>

`pipenv shell` puts you into your work environment. When you're ready to work, or run the code, or install new dependencies, you should be in your pipenv shell.
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>How do I get out of the pipenv shell?</b></summary><p>

Type `exit`.
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>How do I install additional packages from pipenv?</b></summary><p>

```shell
pipenv install packagename
```
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Is it possible to use system-wide packages from inside the virtual environment?</b></summary><p>

This is [not recommended](https://pipenv.readthedocs.io/en/latest/diagnose/#no-module-named-module-name).
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Where are good Python docs?</b></summary><p>

* [Official documentation](https://docs.python.org/3/) tutorial and library reference.

The official docs might be hard to read at first, but you'll get used to them
quickly
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Which linter?</b></summary><p>

Pylint or Flake8. The latter seems to be a bit more popular.
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Can you dynamically add new methods/properties to class through other functions? Or must all properties/methods be declared at once?</b></summary><p>

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
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Following this flow: 1) class Dog is created with attributes size and weight. 2) New instance called Snoopy of class Dog is created. 3) Class Dog gets the method bark() dynamically added to it. Question: will Snoopy now have access to bark() method?</b></summary><p>

Yes.
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>If a subclass inherits from two superclasses with a method of the same name, which method will the subclass use?</b></summary><p>

The answer to this is twofold:

1. Lots of devs and shops frown on multiple inheritance, so maybe just don't do
   it.
   ([Discussion](https://softwareengineering.stackexchange.com/questions/218458/is-there-any-real-reason-multiple-inheritance-is-hated))

2. As for the order in which methods of the same name are resolved, check out
   the [MRO Algorithm](https://en.wikipedia.org/wiki/C3_linearization) which is
   what Python uses.
</p></details></p>


<!-- =============================================================================== -->

<p><details><summary><b>How to handle multiple inheritance and why/when to do it in the first place?</b></summary><p>

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
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Why use tuples instead of lists?</b></summary><p>

* Tuples are immutable. There's a school of thought that says bugs can be reduced if you make as many things immutable as you can.
* Tuples are faster than lists to access.
* Some tuples (containing primitive types), can be used as `dict` keys.
</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>What's the difference between __repr__ and __str__?</b></summary><p>

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

</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>How does <tt>sys.argv</tt> work?</b></summary><p>

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

</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>How do I concatenate two arrays into a single array?</b></summary><p>

Use `extend()`.

```python
a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)

print(a)   # [ 1, 2, 3, 4, 5, 6 ]
```

</p></details></p>

<!-- =============================================================================== -->

## Coding

<!-- =============================================================================== -->

<p><details><summary><b>What are some ways to learn a new language?</b></summary><p>

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

</p></details></p>

<!-- =============================================================================== -->

<p><details><summary><b>Why test code frequently?</b></summary><p>

It's often better to make progress in small increments than to write a bunch of
stuff and test it in one go.

Also, it's easier to stay motivated if you spend 10 minutes getting a first
version going, even if it's missing 99% of its features, and then starting to
iterate on that.
</p></details></p>

<!-- TODO
positional args vs keyword ards
What's the difference between inheritance and polymorphism?

-->

<!-- =============================================================================== -->

<!-- Template:
<p><details><summary><b></b></summary><p>
</p></details></p>

-->