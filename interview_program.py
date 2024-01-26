# 1. Reverse the string

def reverse_the_string(str_1):
    return str_1[::-1]


# print(reverse_the_string('jose antony'))


# 2. Palindrome

def palindrome(str_1):
    return str_1 == str_1[::-1]


# print(palindrome('oppo'))


# 3. Factorial

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


# print(factorial(5))


# 4. Largest number in list

def largest_number(arr):
    lar_num = arr[0]

    for num in arr:
        if num > lar_num:
            lar_num = num

    return lar_num


# print(largest_number([4, 7, 8, 3, 5]))


# 5. Frequency of the numbers

def frequency_of_numbers(arr):
    result = {}

    for num in arr:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1

    return result


# print(frequency_of_numbers([4, 7, 8, 4, 8, 5, 8, 7]))


# 6. Prime Number

def prime_number(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


# print(prime_number(17))


# 7. Second largest

def second_largest(arr):
    sec_lar = 0
    lar = 0

    for num in arr:
        if num > lar:
            sec_lar = lar
            lar = num

        elif num > sec_lar and num != lar:
            sec_lar = num

    return sec_lar


# print(second_largest([4, 7, 8, 3, 5]))


# 8. Sort(bubble sort)

def sort_the_list(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


my_list = [4, 7, 8, 3, 5]
sort_the_list(my_list)


# print(my_list)


# 9. Reverse the list or string

def reverse_list(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


rev_list = [4, 7, 8, 3, 5]
rev_str = list("jose antony")

reverse_list(rev_list)
# print(rev_list)

reverse_list(rev_str)


# print("".join(rev_str))


# 10. Two sum

def two_sum(arr, tot):
    seen = {}

    for i, num in enumerate(arr):
        complement = tot - num
        if complement in seen:
            return [num, complement]

        seen[num] = i


target = 9
my_list = [4, 7, 8, 3, 5]


# print(two_sum(my_list, target))


# 11. Max sub array sum

def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# 12. Anagram

def is_anagram(s, t):
    print(sorted(s))
    print(sorted(t))
    return sorted(s) == sorted(t)


string1 = "listen"
string2 = "silent"
# print(is_anagram(string1, string2))


# 13

new_list = [4, 9, 2, 5, 7]
new_str = "jose antony"

print(sorted(new_list))  # sort the list
print("".join(sorted(new_str)))  # sort the str

new_list.sort()  # sort the list
print(new_list)

new_list.reverse()  # reverse the list
print(new_list)

# 14. Merge two sorted array


# 15. otp - a3b5c3a3
from itertools import groupby


def compress_string(inp_str):
    out_str = ""

    for char, group in groupby(inp_str):
        out_str += char + str(len(list(group)))

    return out_str


input_str = "aaabbbbbcccaaa"
output = compress_string(input_str)
print(output)

# 16.
"""
output - 

Rank of Virat is 1
Rank of Rahul is 2
Rank of Rohit is 3
"""


# total_marks = {student: sum(mark.values()) for student, mark in s.items()}
# print(total_marks)
#
# order_students = sorted(total_marks.keys(), key=lambda student: total_marks[student], reverse=True)
# print(order_students)
#
# order_by_rank = {student: rank + 1 for rank, student in enumerate(order_students)}
# print(order_by_rank)
#
# for student in order_by_rank:
#     print(f"Rank of {student} is {order_by_rank[student]}")


# 17. Find Kth Largest Element in an Array

def find_kth_largest(nums, k):
    return sorted(nums)[-k]


# 18. missing number

def missing_number(n):
    numbers = set(n)
    out_put = []

    for i in range(1, n[-1]):
        if i not in numbers:
            out_put.append(i)

    return out_put


input_numbers = [0, 1, 3, 4, 5]
result = missing_number(input_numbers)
print(f"The missing number is: {result}")

# 19. output should be - ['Gfg', 'Best', 'Reading CS']

import re

str_1 = "‘<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it.’"  # tag = “b”

obj = re.findall(r"<b>.*?</b>", str_1)

out_li = []
for i in obj:
    # print(type(i).__dict__)
    sen = i.replace('<b>', "").replace('</b>', "")
    out_li.append(sen)

print(out_li)


# 20. decorator

def check_odd_arguments(func):
    def wrapper(x, y):
        if x % 2 != 0 and y % 2 != 0:
            return func(x, y)
        else:
            return "Both arguments must be odd."

    return wrapper


@check_odd_arguments
def multiply_odd_numbers(a, b):
    return a * b


result = multiply_odd_numbers(3, 5)
print(result)


# 21. list, tuple, set, dict based operation

# (i)
tuple_ = (1, [2, 3, 4])  # tuple immutable

tuple_[1].append(5)  # list mutable

print(tuple_)

# (ii) slicing

my_list = [1, 2, 3, 4, 5]  # output - [4,3,2]

print(my_list[3:0:-1])

my_list = [2, 3, 4, 5]  # output - [4,3,2]

print(my_list[2::-1])


# 22. given values for x,y and an array A of size N.print the value that are in between x and y?

def values_in_range(arr, x, y):
    result = [element for element in arr if x <= element <= y]
    return result

# Example usage:
arr = [1, 5, 3, 8, 12, 7, 15, 6]
x = 4
y = 10

result = values_in_range(arr, x, y)
print("Values in the range [{}, {}]: {}".format(x, y, result))


# 23. given an array A, find the sum of elements present in specified gap N inputs?

def sum_in_gaps(arr, gap):
    result = 0

    for i in range(0, len(arr), gap):
        result += arr[i]

    return result

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gap = 2

result = sum_in_gaps(arr, gap)
print("Sum of elements in specified gaps of size", gap, ":", result)


# 24. input - a1b5c2a3, output - abbbbbccaaa

import re

def transform_string(input_str):
    result = ''
    pattern = re.compile(r'([a-zA-Z])(\d*)')

    matches = pattern.findall(input_str)

    for char, count in matches:
        count = int(count) if count else 1
        result += char * count

    return result

# Example usage:
input_str = 'a1b5c2a3'
output_str = transform_string(input_str)
print("Transformed string:", output_str)


# 25. Train ticket booking system

class Train:
    def __init__(self, train_id, name, source, destination, capacity):
        self.train_id = train_id
        self.name = name
        self.source = source
        self.destination = destination
        self.capacity = capacity
        self.booked_seats = 0

    def check_availability(self):
        return self.capacity - self.booked_seats

    def book_tickets(self, num_tickets):
        available_seats = self.check_availability()

        if num_tickets <= available_seats:
            self.booked_seats += num_tickets
            print(f"Booking successful for {num_tickets} seats in {self.name}")
            return True
        else:
            print(f"Sorry, only {available_seats} seats available in {self.name}")
            return False


class BookingSystem:
    def __init__(self):
        self.trains = {}

    def add_train(self, train):
        self.trains[train.train_id] = train

    def book_tickets(self, train_id, num_tickets):
        if train_id in self.trains:
            return self.trains[train_id].book_tickets(num_tickets)
        else:
            print("Invalid Train ID")
            return False


# Example usage:
if __name__ == "__main__":
    # Creating Train objects
    train1 = Train(1, "Express1", "CityA", "CityB", 100)
    train2 = Train(2, "Express2", "CityB", "CityC", 80)

    # Creating BookingSystem object
    booking_system = BookingSystem()

    # Adding trains to the system
    booking_system.add_train(train1)
    booking_system.add_train(train2)

    # Booking tickets
    booking_system.book_tickets(1, 50)
    booking_system.book_tickets(2, 30)
    booking_system.book_tickets(1, 70)  # Attempt to book more seats than available


# 26. print the maximum number of characters present in between the two same characters?

def max_chars_between_same(input_str):
    max_distance = 0
    char_positions = {}

    for i, char in enumerate(input_str):
        if char in char_positions:
            distance = i - char_positions[char] - 1
            max_distance = max(max_distance, distance)

        char_positions[char] = i

    return max_distance

# Example usage:
input_str = 'abcdbce'
result = max_chars_between_same(input_str)
print("Maximum number of characters between the same characters:", result)
