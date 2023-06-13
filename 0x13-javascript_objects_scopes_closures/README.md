# 0x13. JavaScript - Objects, Scopes and Closures
### `JavaScript`
## Resources
**Read or watch**:

* [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
* [Object-oriented JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript) (***read all examples!***)
* [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
* [super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
* [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
* [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
* [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
* [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/ClosuresB)
* [this/self](https://alistapart.com/article/getoutbindingsituations/)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## General
* Why JavaScript programming is amazing
* How to create an object in JavaScript
* What this means
* What undefined means
* Why the variable type and scope is important
* What is a closure
* What is a prototype
* How to inherit an object from another

## Requirements
###General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 20.04 LTS using node (version `14.x`)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/node`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be `semistandard` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
* All your files must be executable
* The length of your files will be tested using `wc`
* You are not allowed to use `var`

## More Info
### Install Node 14
```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
### Install semi-standard
[Documentation](https://github.com/standard/semistandard)
```
$ sudo npm install semistandard --global
```

## Tasks

[0. Rectangle #0](./0-rectangle.js)

Write an empty class `Rectangle` that defines a rectangle:

* You must use the `class` notation for defining your class
```
guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Class: Rectangle]
guillaume@ubuntu:~/0x13$
```

[1. Rectangle #1](./1-rectangle.js)

Write a class `Rectangle` that defines a rectangle:

* You must use the `class` notation for defining your class
* The constructor must take **2** arguments `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`
```
guillaume@ubuntu:~/0x13$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$
```

[2. Rectangle #2](./2-rectangle.js)

Write a class `Rectangle` that defines a rectangle:

* You must use the `class` notation for defining your class
* The constructor must take **2** arguments `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`
* If `w` or `h` is equal to `0` or not a positive integer, create an empty object
```
guillaume@ubuntu:~/0x13$ cat 2-main.js
#!/usr/bin/node
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);

guillaume@ubuntu:~/0x13$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
guillaume@ubuntu:~/0x13$
```

[3. Rectangle #3](./3-rectangle.js)

Write a class `Rectangle` that defines a rectangle:

* You must use the `class` notation for defining your class
* The constructor must take **2** arguments: `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`
* If `w` or `h` is equal to 0 or not a positive integer, create an empty object
* Create an instance method called `print()` that prints the rectangle using the character `X`
```
guillaume@ubuntu:~/0x13$ cat 3-main.js
#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

guillaume@ubuntu:~/0x13$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
guillaume@ubuntu:~/0x13$
```

[4. Rectangle #4](./4-rectangle.js)

Write a class `Rectangle` that defines a rectangle:

* You must use the `class` notation for defining your class
* The constructor must take **2** arguments: `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`
* If `w` or `h` is equal to 0 or not a positive integer, create an empty object
* Create an instance method called `print()` that prints the rectangle using the character `X`
* Create an instance method called `rotate()` that exchanges the `width` and the `heigh`t of the rectangle
* Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by `2`
```
guillaume@ubuntu:~/0x13$ cat 4-main.js
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

guillaume@ubuntu:~/0x13$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x13$
```
