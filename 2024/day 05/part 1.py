with open("2024/day 05/input.txt") as f:
    f = f.read().strip()
    ordering, produce = f.split("\n\n")
    ordering = ordering.split("\n")
    produce = produce.split("\n")

edges = {}

for row in ordering:
    first_num, second_num = map(int, row.split("|"))
    if first_num not in edges:
        edges[first_num] = set()
    edges[first_num].add(second_num)

sum = 0

for row in produce:
    correct = True
    row = list(map(int, row.split(",")))
    for i in range(len(row)-1):
        if row[i+1] in edges and row[i] in edges[row[i+1]]:
            correct = False
            break
    
    if correct:
        sum += row[len(row)//2]

print(sum)