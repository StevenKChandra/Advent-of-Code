left_list = []
right_table = {}

with open("2024/day 01/input.txt") as f:
    for line in f:
        first_num, second_num = line.split()
        left_list.append(int(first_num))
        if int(second_num) not in right_table:
            right_table[int(second_num)] = 0
        right_table[int(second_num)] += 1

total = 0

for num in left_list:
    if num in right_table:
        total += num * right_table[num]

print(total)