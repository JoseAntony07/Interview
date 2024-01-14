s = {'Rahul': {'English': 70, 'Maths': 66, 'Science': 80},
     'Virat': {'English': 58, 'Maths': 88, 'Science': 72},
     'Rohit': {'English': 91, 'Maths': 40, 'Science': 65}}

person_dict = dict()

# 1. (i)
for k, v in s.items():
    for sub, mark in v.items():
        if k in person_dict:
            person_dict[k] += mark
        else:
            person_dict[k] = mark

# print(mark)

# 1. (ii)

total_marks = {student: sum(mark.values()) for student, mark in s.items()}
print(total_marks)

order_students = sorted(total_marks.keys(), key=lambda student: total_marks[student], reverse=True)
print(order_students)

order_by_rank = {student: rank + 1 for rank, student in enumerate(order_students)}
print(order_by_rank)

for student in order_by_rank:
    print(f"Rank of {student} is {order_by_rank[student]}")

# 2. (i)
input_str = "aaabbbbbcccaaa"

output = 'a3b5c3a3'

out_put = ""
most_occurence = {}

for val in list("".join(input_str)):
    if val in most_occurence:
        most_occurence[val] += 1
    else:
        most_occurence[val] = 1

print(most_occurence)

concat = ""

for k, val in most_occurence.items():
    concat += f"{k}{val}"

print(concat)

# 2. (ii)

from itertools import groupby


def compress_string(inp_str):
    out_str = ""

    for char, group in groupby(inp_str):
        print(char)
        print(list(group))
        out_str += char + str(len(list(group)))

    return out_str


input_str = "aaabbbbbcccaaa"
output = compress_string(input_str)
print(output)
