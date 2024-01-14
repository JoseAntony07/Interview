import pickle
import os
from pathlib import Path

file_dir = '..'

base_dir = Path(__file__).resolve().parent
print(base_dir)

file_dir_ = base_dir

files = os.listdir(file_dir_)

print(files)

for file in files:
    print(file)


files = [file for file in os.listdir(file_dir_) if os.path.isfile(os.path.join(file_dir, file))]
print(files)


file_path = '/home/siam-jose/ExpenseProject/Test/algo.py'

with open(file_path, 'r') as file:
    for line in file:
        print(line)


a = b = 3
print(a is b)


def simple(num):
    for i in range(num):
        yield i * 2


for j in simple(5):
    print(j)


my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

print(my_iter)

print(next(my_iter))


data = {'name': 'John', 'age': 30, 'city': 'New York'}

# with open('data.pkl', 'wb') as file:
#     pickle.dump(data, file)


with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)
