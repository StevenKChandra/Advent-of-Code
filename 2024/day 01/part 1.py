left_list = []
right_list = []

with open("2024/day 01/input.txt") as f:
    for line in f:
        left_num, right_num = line.split()
        left_list.append(int(left_num))
        right_list.append(int(right_num))

left_list.sort()
right_list.sort()

total = 0

for i in range(len(left_list)):
    total += abs(left_list[i] - right_list[i])

print(total)