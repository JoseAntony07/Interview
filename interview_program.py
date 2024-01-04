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
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


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
