# 0x01. Python - if/else, loops, functions

## Resourcs
**Read or watch**
* [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (Read until “4.6. Defining Functions” included)
* [IndentationError](https://www.youtube.com/watch?v=1QXOd2ZQs-Q)
* [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
* [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Learn to Program 2 : Looping](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)
**man or help**
* `python3`
## Requirements
### Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version `2.8.*`)
* All your files must be executable
* The length of your files will be tested using `wc`
### C Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
* All your files should end with a new line
* Your code should use the `Betty` style. It will be checked using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl)
* You are not allowed to use global variables
* No more than 5 functions per file
* In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples
* The prototypes of all your functions should be included in your header file called `lists.h`
* Don’t forget to push your header file
* All your header files should be include guarded
## Tasks
[0. Positive anything is better than negative nothing](./0-positive_or_negative.py)

This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.
* You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py)
* The variable `number` will store a different value every time you will run this program
* You don’t have to understand what `import`, `random. randint` do. Please do not touch this code
* The output of the program should be:
	* The number, followed by
		* if the number is greater than 0: `is positive`
		* if the number is 0: `is zero`
		* if the number is less than 0: `is negative`
	* followed by a new line
```
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-3 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-10 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
10 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-5 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
6 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
7 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
5 is positive
guillaume@ubuntu:~/0x01$
```
