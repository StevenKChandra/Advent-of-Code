with open("2024/day 09/input.txt", "r") as f:
    disk_map = f.read().strip()

spaces = disk_map[1::2]
blocks = disk_map[::2]

m = len(spaces)
n = len(blocks)

file_ID_front = 0
file_ID_back = n - 1

check_sum = 0
sequence_counter = 0
remainder = int(blocks[file_ID_back])

while file_ID_front <= file_ID_back:

    block_to_fill = int(blocks[file_ID_front])
    check_sum += block_to_fill * (2 * sequence_counter + block_to_fill - 1) * file_ID_front / 2
    sequence_counter += block_to_fill
    file_ID_front += 1

    if file_ID_back == 5350:
        pass

    if file_ID_front >= file_ID_back:
        break
    
    space_to_fill = int(spaces[file_ID_front - 1])

    while space_to_fill >= remainder:
        check_sum += remainder * (2 * sequence_counter + remainder - 1) * file_ID_back / 2
        sequence_counter += remainder
        space_to_fill -= remainder
        file_ID_back -= 1
        remainder = int(blocks[file_ID_back])
    
    if file_ID_front >= file_ID_back:
        remainder = 0
        break

    check_sum += space_to_fill * (2 * sequence_counter + space_to_fill - 1) * file_ID_back / 2
    sequence_counter += space_to_fill
    remainder -= space_to_fill

check_sum += remainder * (2 * sequence_counter + remainder - 1) * file_ID_back / 2

print(check_sum)