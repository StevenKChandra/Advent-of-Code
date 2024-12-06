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

def fix_ordering(row, edges, i):
    row[i], row[i+1] = row[i+1], row[i]
    if i > 0 and row[i] in edges and row[i-1] in edges[row[i]]:
        fix_ordering(row, edges, i-1)

for row in produce:
    correct = True
    row = list(map(int, row.split(",")))
    for i in range(len(row)-1):
        if row[i+1] in edges and row[i] in edges[row[i+1]]:
            correct = False
            fix_ordering(row, edges, i)

    if not correct:
        sum += row[len(row)//2]

print(sum)