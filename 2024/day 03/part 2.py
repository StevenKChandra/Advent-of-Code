import re

total = 0

with open("2024/day 03/input.txt") as f:
    input = f.read()

matches = re.findall("(do\(\)|don't\(\)|mul\([0-9]+,[0-9]+\))", input)

do = True
for match in matches:
    if match == "do()":
        do = True
        continue

    if match == "don't()":
        do = False
        continue
    
    if do:
        mul = re.findall("mul\([0-9]+,[0-9]+\)", match)
        mul = re.findall("[0-9]+", mul[0])
        total += int(mul[0]) * int(mul[1])

print(total)