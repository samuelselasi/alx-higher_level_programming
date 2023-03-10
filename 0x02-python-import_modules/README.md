# 0x02. Python - import & modules
## Resources
**Read or watch**:
* [Modules](https://docs.python.org/3/tutorial/modules.html)
* [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
* [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)
**man or help:**

`python3`
## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version `2.8.*`)
* All your files must be executable
* The length of your files will be tested using `wc`
## Tasks
[0. Import a simple function from a simple file](./0-add.py)

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`

* You have to use `print` function with string format to display integers
* You have to assign:
	* the value `1` to a variable called `a`
	* the value `2` to a variable called `b`
	* and use those two variables as arguments when calling the functions `add` and `print`
* `a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`
* Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
* You can only use the word `add_0` once in your code
* You are not allowed to use `*` for importing or `__import__`
* Your code should not be executed when imported - by using `__import__`, like the example below
```
guillaume@ubuntu:~/0x02$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

guillaume@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/0x02$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/0x02$ python3 0-import_add.py
guillaume@ubuntu:~/0x02$
```
[1. My first toolbox!](./1-calculation.py)

Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.

* Do not use the function `print` (with string format to display integers) more than 4 times
* You have to define:
	* the value `10` to a variable `a`
	* the value `5` to a variable `b`
	* and use those two variables only, as arguments when calling functions (including `print`)
* `a` and `b` must be defined in 2 different lines: `a = 10` and another `b = 5`
* Your program should call each of the imported functions. See example below for format
* the word `calculator_1` should be used only once in your file
* You are not allowed to use `*` for importing or `__import__`
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

guillaume@ubuntu:~/0x02$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
guillaume@ubuntu:~/0x02$
```
