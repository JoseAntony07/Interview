def reverse_list(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]

        start += 1
        end -= 1


inp_list = [1, 2, 3, 4, 5]
reverse_list(inp_list)
print(inp_list)

inp_str = list("".join('jose antony'))
print(inp_str)

reverse_list(inp_str)
print("".join(inp_str))


# time complexity of O(n/2)
# it modifies the original string/list without creating a new one


def bubble_sort(elements):
    n = len(elements)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]


# Test the function
nums = [5, 2, 8, 1, 9]
bubble_sort(nums)
print(nums)


# 1. Explain time complexity and space complexity.

"""
Answer: Time complexity represents the amount of time an algorithm takes with respect to the input size.
 Space complexity represents the amount of memory an algorithm uses with respect to the input size. 
 Both are commonly expressed using Big O notation.
"""
