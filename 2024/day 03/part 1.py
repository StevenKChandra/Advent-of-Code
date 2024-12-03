import re

total = 0

with open("2024/day 03/input.txt") as f:
    input = f.read()

matches = re.findall("mul\([0-9]+,[0-9]+\)", input)

for multiplication in matches:
    multiplication = re.findall("[0-9]+", multiplication)
    total += int(multiplication[0]) * int(multiplication[1])

print(total)