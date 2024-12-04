def find(input, i, j, m, n, pattern):
    if input[i][j] != pattern[0]:
        return 0

    l = len(pattern)
    combinations = [
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
    ]

    count = 0
    for com in combinations:
        x = com[0] * (l - 1)
        y = com[1] * (l - 1)
        if i + x >= 0 and i + x < m and j + y >= 0 and j + y < n:
            for k in range(1, l):
                if input[i + k * com[0]][j + k * com[1]] != pattern[k]:
                    k -= 1
                    break

            if k == l - 1:
                count += 1

    return count

with open("2024/day 04/input.txt") as f:
    input = f.read().strip().split("\n")    

PATTERN = ["X", "M", "A", "S"]

m = len(input)
n = len(input[0])

count = 0

for i in range(m):
    for j in range(n):
        count += find(input, i, j, m, n, PATTERN)
    
print(count)
                           