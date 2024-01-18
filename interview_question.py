

"""
1) Explain time complexity and space complexity?

-> Time complexity represents the amount of time an algorithm takes with respect to the input size.
 Space complexity represents the amount of memory an algorithm uses with respect to the input size.
 Both are commonly expressed using Big O notation.

2) How python works?

python program run by interpreter
|
interpreter run the code and break into small pieces called token
|
interpreter organize the tokens into structure are called parse tree(to understand the structure of program)
|
interpreter convert parse tree to bytecode
|
interpreter convert bytecode to machine code(computer processor can understand)

3) Memory managed in python?

-> memory management in python is handled by "python memory manager".
-> memory allocated by manager is in form of a "private heap space".
-> it is inaccessible to the programmer.
-> python has in built "garbage collector" for recycle the un used memory in private heap space.

4) Namespace?

-> it ensure that objects names in program are unique and can be used without any conflict
-> local - cycle of function
-> global - cycle of script file/import package
-> built in - exception and etc

5) shallow copy vs deep copy?


6) range and xrange?


7) Pickling and Unpickling?


8) Generators?


9) GIL? (global interpreter lock)

- Preventing multiple native threads from executing Python bytecodes at once
- Only one thread can execute python a time
- It can impact multithreading programs by limiting parallelism

10) constructor? (__init__)

- constructor is a special method that is automatically called when an object is created.
The purpose of a constructor is to initialize the attributes (properties) of the object

11) py2 vs py3?


12) unicode, encode, decode?


13) Thread pool and Thread pool executor?

Thread Pool:

- A group of ready-to-use threads that are kept in reserve to do tasks when needed.
- Think of it like having a team of workers waiting to perform various jobs.

ThreadPoolExecutor:

- In Python, this is a specific tool (a class) that helps you manage and use a thread pool.
- It's like a manager for your team of workers (threads), helping you assign tasks, keep track of their progress,
  and make sure things run smoothly.


14) multi threading vs multiprocessing?

Multithreading:

Idea: Imagine you're a chef in a kitchen, and you have multiple assistants (threads) helping you.

Note: In some kitchens (like Python's default interpreter CPython), there's a rule that only one person can use the
      main chopping board at a time (Global Interpreter Lock or GIL).

Multiprocessing:

Idea: Picture having multiple independent kitchens (processes), each with its own chef.
     They can work on different recipes simultaneously.

Note: Each kitchen has its own set of tools (memory), so chefs (processes) don't accidentally mess with each other's ingredients.


- multithreading is like having multiple helpers in the same kitchen, and multiprocessing is like having entirely
 separate kitchens with their own chefs.


15) Thread Lock?

- Imagine you have a shared toy, and many kids (threads) want to play with it at the same time.
- A thread lock is like a rule that only one kid can play with the toy at any given moment.
- If another kid (thread) is already playing (holds the lock), the new kid has to wait until the toy is free.
- a thread lock ensures that only one thread can access a shared resource or code section at a time, avoiding conflicts
  and ensuring things stay in order.


16) What is Python, and why is it used?

- Python is a high-level, interpreted programming language that is widely used for web development, scientific
  computing, data analysis, artificial intelligence.
- Python’s extensive library and community support make it a versatile language suitable for a wide range of applications.


17) Explain the difference between a list and a tuple in Python?

- In Python, a list and a tuple are both used to store a collection of values
- A list is mutable, which means you can add, remove, or modify elements after creating the list.
  A tuple, on the other hand, is immutable, meaning you cannot modify its contents once it has been created.

tuple ex:  a pair of latitude and longitude coordinates representing a location.


18) How can python be an interpreted language?

- Python is an interpreted language because it is executed directly by the interpreter, without the need for compilation.
- The Python interpreter reads each line of code in a program and translates it to machine code or bytecode.


19) What is the Dogpile effect?

- Imagine you have a shelf with cookies, and people can take cookies from this shelf.
You want to make sure that the cookies on the shelf are always fresh.

Fresh Cookies (Cache) - Initially, you have a plate of fresh cookies on the shelf.

Taking Cookies (Requests) - People come and take cookies from the shelf. As long as there are cookies, everyone is happy.

Empty Plate (Cache Miss) - Eventually, the plate becomes empty, and you need to put new cookies on it.

First Person (First Request) - The first person notices the empty plate, so they go to the kitchen, bake new cookies,
                               and put them on the plate.

Other People (Subsequent Requests) - While the first person is baking, other people also see the empty plate and decide
                                     to bake new cookies themselves.

Simultaneous Baking (Simultaneous Recalculation) - Now, multiple people are in the kitchen baking cookies at the
                                                   same time, not realizing that the first person is already doing it.


- So, the "Dogpile effect" is like a situation where everyone sees an empty plate, decides to bake new cookies
  simultaneously, creating a bit of chaos and inefficiency in the process.

- In the world of computer systems, this relates to multiple requests trying to update or recalculate the same
  information in a cache at the same time, causing some inefficiencies. Strategies are used to manage this situation
  and ensure a smoother process.


20) What is PYTHONPATH in python??

- PYTHONPATH is an environment variable in Python that tells the interpreter where to look for modules and packages
  when you execute a script or run a Python program.


21) Why zip() function is used?

- The zip() function in Python is used to combine elements from two or more iterable objects (such as lists, tuples, or strings) into tuples.
- It creates an iterator that generates tuples containing elements.

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]

# zip
paired_data = zip(names, ages)
print(paired_data)  # <zip object at 0x7fb3d82e64c0>  (iterator object)

list_data = list(paired_data)
print(list_data)  # [('Alice', 25), ('Bob', 30), ('Charlie', 22)]

dict_data = dict(paired_data)
print(dict_data)   # {'Alice': 25, 'Bob': 30, 'Charlie': 22}


# unzip
name, age = zip(*list_data)
print(name)  # ('Alice', 'Bob', 'Charlie')


name, age = zip(*dict_data.items())
print(age)  # (25, 30, 22)


22) What is PEP 8, and why is it important?

- PEP 8 stands for "Python Enhancement Proposal 8." It is a style guide for writing clean, readable, and consistent
  Python code. The primary goal of PEP 8 is to improve the readability of code.

"""
