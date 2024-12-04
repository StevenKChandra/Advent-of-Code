def find_xmas(input, i, j):
    M_posititons = [
        (-1, -1, 1, -1),
        (-1, -1, -1, 1),
        (1, -1, 1, 1),
        (-1, 1, 1, 1),
    ]

    for position in M_posititons:
        first_M = input[i + position[0]][j + position[1]]
        second_M = input[i + position[2]][j + position[3]]
        first_S = input[i - position[0]][j - position[1]]
        second_S = input[i - position[2]][j - position[3]]

        if  first_M == "M" and second_M == "M" and first_S == "S" and second_S == "S":
            return True
    
    return False

with open("2024/day 04/input.txt") as f:
    input = f.read().strip().split("\n")    

m = len(input)
n = len(input[0])

count = 0

for i in range(1, m-1):
    for j in range(1, n-1):
        if input[i][j] == "A" and find_xmas(input, i, j):
            count += 1
    
print(count)
                           