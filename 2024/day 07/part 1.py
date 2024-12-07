with open("2024/day 07/input.txt") as f:
    input = f.read().strip().split("\n")

total = 0

def operate(numbers):
    output = [numbers[0]]

    for number in numbers[1:]:
        placeholder = []
        for item in output:
            placeholder.append(item + number)
            placeholder.append(item * number)
        output = placeholder

    return output

for row in input:
    target, numbers = row.split(": ")

    target = int(target)
    numbers = list(map(int, numbers.split()))

    if target in operate(numbers):
        total += target

print(total)