# 0x04. Python - More Data Structures: Set, Dictionary
## Resources
**Read or watch**:
* [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
* [Lambda, filter, reduce and map](https://python-course.eu/advanced-python/lambda-filter-reduce-map.php)
* [Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)
**man or help**:
* `python3`
## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version` 2.8.*`)
* All your files must be executable
* The length of your files will be tested using `wc`
## Tasks
[0. Squared simple](./0-square_matrix_simple.py)

Write a function that computes the square value of all integers of a matrix.

* Prototype: `def square_matrix_simple(matrix=[]):`
* `matrix` is a 2 dimensional array
* Returns a new matrix:
	* Same size as `matrix`
	* Each value should be the square of the value of the input
* Initial matrix should not be modified
* You are not allowed to import any module
* You are allowed to use regular loops, `map`, etc.
```
guillaume@ubuntu:~/0x04$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/0x04$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$
```
[1. Search and replace](./1-search_replace.py)

Write a function that replaces all occurrences of an element by another in a new list.

* Prototype: `def search_replace(my_list, search, replace):`
* `my_list` is the initial list
* `search` is the element to replace in the list
* `replace` is the new element
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x04$ cat 1-main.py
#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x04$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
guillaume@ubuntu:~/0x04$
```
