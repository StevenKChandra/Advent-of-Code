with open("2024/day 09/input.txt", "r") as f:
    disk_map = f.read().strip()

spaces = list(map(int,disk_map[1::2]))
spaces.append(0)
blocks = list(map(int,disk_map[::2]))

blocks_copy = blocks.copy()
spaces_copy = spaces.copy()

n = len(blocks)

check_sum = 0

for i in reversed(range(n)):
    sequence_counter = 0
    for j in range(i):
        sequence_counter += int(blocks[j])
        if blocks_copy[i] <= spaces[j]:
            check_sum += blocks_copy[i] * (2 * sequence_counter + blocks_copy[i] - 1) * i / 2
            spaces[j] -= blocks_copy[i]
            blocks[j] += blocks_copy[i]
            blocks[i] = 0
            break
        sequence_counter += spaces[j]

sequence_counter = 0
for i in range(n):
    if blocks[i] != 0:
        check_sum += blocks_copy[i] * (2 * sequence_counter + blocks_copy[i] - 1) * i / 2
    sequence_counter += blocks_copy[i] + spaces_copy[i]

print(check_sum)