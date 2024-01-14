

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

"""
