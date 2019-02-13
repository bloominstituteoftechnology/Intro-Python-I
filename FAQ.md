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

## Python

<p><details><summary><b>Are there any helpful VS Code extensions that are recommend for using with Python?</b></summary><p>

* [Official VS Code Python Extension](https://code.visualstudio.com/docs/languages/python)
</p></details></p>

<p><details><summary><b>I'm on Windows; what command do I use to run Python?</b></summary><p>

If you're running in PowerShell or cmd, use:

```
py
```

If in bash, use `python` or `python3`.
</p></details></p>

<p><details><summary><b>What version of Python do I need?</b></summary><p>

You should have version 3.7 or higher. Test with:

```shell
python --version
```
</p></details></p>


<p><details><summary><b>Do I need to use pipenv?</b></summary><p>

You should. Good Python devs know how.
</p></details></p>


<p><details><summary><b>How do I get out of the Python REPL?</b></summary><p>

Hit `CTRL-D`. This is the way End-Of-File is signified in Unix-likes.
</p></details></p>


<p><details><summary><b>What does "REPL" mean?</b></summary><p>

_Read, Evaluate, Print Loop_.

It reads your input, evaluates it, and prints the result. And loops.
</p></details></p>

<p><details><summary><b>I'm on a Mac and when I run Python it says I'm on version 2.7. Why?</b></summary><p>

Macs come with version 2.7 by default. You'll need to install version 3.

And preferable use `pipenv` after that.
</p></details></p>

<p><details><summary><b>Does Python use tabs or spaces?</b></summary><p>

[PEP 8](https://www.python.org/dev/peps/pep-0008/) says four spaces.
</p></details></p>

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

<p><details><summary><b>Does Python have hoisting?</b></summary><p>

No.

[What is hoisting?](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
</p></details></p>

<p><details><summary><b>Does scoping work similar to other languages?</b></summary><p>

Generally, and also not really. Variables are either global or function-local.

Since there are no declarations, there's no block-level scope.

It is similar to `var` in JavaScript.
</p></details></p>

<p><details><summary><b>Can you return a reference to a function from another function? Or store it in a variable?</b></summary><p>

Yes. Functions are [first-class citizens](https://en.wikipedia.org/wiki/First-class_citizen).
</p></details></p>

<p><details><summary><b>Can you use boolean shortcut assignments?</b></summary><p>

Yes, you can. This is common in Perl and JavaScript, but it's not particularly [idiomatic](https://en.wikipedia.org/wiki/Programming_idiom) in Python.

```python
x = SomethingFalsey or 5
```
</p></details></p>

<p><details><summary><b>Can you do anonymous functions?</b></summary><p>

You can use `lambda` for simple functions:

```python
adder = lambda x, y: x + y

adder(4, 5)   # 9

do_some_math(4, 5, lambda x, y: y - x)
```
</p></details></p>

<p><details><summary><b>Is a dict like a JavaScript object?</b></summary><p>

Sort of.

The syntax is different, though. In Python you must use `[]` notation to access elements. And you must use `"` around the key names.
</p></details></p>

<p><details><summary><b>What are all those method names with double underscores around them?</b></summary><p>

Those are function you typically don't need to use, but can override or call if you wish.

Most commonly used are:

* `__init__()` is the constructor for objects
* `__str__()` returns a string representation of the object
* `__repr__()` returns a string representation of the object, for debugging
</p></details></p>

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

<p><details><summary><b>When do we run pipenv shell?</b></summary><p>

`pipenv shell` puts you into your work environment. When you're ready to work, or run the code, or install new dependencies, you should be in your pipenv shell.
</p></details></p>

<p><details><summary><b>How do I get out of the pipenv shell?</b></summary><p>

Type `exit`.
</p></details></p>

<p><details><summary><b>How do I install additional packages from pipenv?</b></summary><p>

```shell
pipenv install packagename
```
</p></details></p>

<p><details><summary><b>Is it possible to use system-wide packages from inside the virtual environment?</b></summary><p>

This is [not recommended](https://pipenv.readthedocs.io/en/latest/diagnose/#no-module-named-module-name).
</p></details></p>

<p><details><summary><b>Where are good Python docs?</b></summary><p>

* [Official documentation](https://docs.python.org/3/) tutorial and library reference.

The official docs might be hard to read at first, but you'll get used to them
quickly
</p></details></p>

<p><details><summary><b>Which linter?</b></summary><p>

Pylint or Flake8. The latter seems to be a bit more popular.
</p></details></p>

## Coding

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

<p><details><summary><b>Why test code frequently?</b></summary><p>

It's often better to make progress in small increments than to write a bunch of
stuff and test it in one go.

Also, it's easier to stay motivated if you spend 10 minutes getting a first
version going, even if it's missing 99% of its features, and then starting to
iterate on that.
</p></details></p>

