# https://www.interviewbit.com/python-interview-questions/#memory-management-in-python
# https://medium.com/@nikitasilaparasetty/python-interview-coding-questions-with-solutions-for-beginners-7f6d782defac


def mul(a, b):
    print(a * b)


mul(4, 5)

mul = lambda a, b: a * b

# print(mul(3, 2))


import copy

original_list = [1, [2, 3], 4]
shallow_copied_list = copy.copy(original_list)

# Modify the nested list in the shallow copy
shallow_copied_list[1][0] = 99
shallow_copied_list[0] = 8

print(original_list)        # [1, [99, 3], 4]
print(shallow_copied_list)

print('==============================================================')

original_list_ = [1, [2, 3], 4]
deep_copied_list = copy.deepcopy(original_list_)

# Modify the nested list in the deep copy
deep_copied_list[1][0] = 99
deep_copied_list[0] = 8


print(original_list_)
print(deep_copied_list)


my_list = range(5)
# print(list(my_list))


"""
I'm Jose Antony, based in Chennai, with over 3 years of experience as a Python developer.
 During this time, I have successfully contributed to three distinct projects.

Project: Fyxt

Fyxt is a comprehensive property management system designed to facilitate seamless communication between property
 owners, tenants, and vendors. The platform streamlines issue resolution, such as plumbing concerns, by utilizing 
 a ticketing system. In this project, I implemented the multi-tenant concept, replica mail behavior, chat functionality,
  ticket management, and service planning.
  
Project: Marlo

Marlo focuses on providing loan products, particularly for ship owners. It extends its services to non-ship owners as
 well, allowing them to apply for loans related to their voyage processes. The project incorporates features like
  vessel tracking and loan application management using technologies such as CRM, Django, GraphQL, and PostgreSQL.
  
Project: Kauvery Kare Application

The Kauvery Kare Application serves as the official app for Kauvery Hospital, offering patients a seamless experience
 for booking both online and offline appointments, video calling, master health checkups, and managing health records.
  This microservices project employs technologies like FastAPI, Django, Kafka, and integrates various third-party tools.

"""

# How python works
"""
python program run by interpreter
|
interpreter run the code and break into small pieces called token
|
interpreter organize the tokens into structure are called parse tree(to understand the structure of program)
|
interpreter convert parse tree to bytecode
|
interpreter convert bytecode to machine code(computer processor can understand)
"""

# Memory managed in python
"""
-> memory management in python is handled by "python memory manager".
-> memory allocated by manager is in form of a "private heap space".
-> it is inaccessible to the programmer.
-> python has in built "garbage collector" for recycle the un used memory in private heap space.
"""

# Namespace
"""
-> it ensure that objects names in program are unique and can be used without any conflict
-> local - cycle of function
-> global - cycle of script file/import package  
-> built in - exception and etc
"""


mul_ = lambda a, b: a * b

print(mul_(2, 3))

my_list_ = [1, 2, 3, 4]

res = list(map(lambda a: a ** 2, my_list_))
print(res)

names = ["Alice", "Bob", "Charlie"]
res_ = list(map(str.upper, names))
print(res_)
