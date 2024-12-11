with open("2024/day 11/input.txt") as f:
    numbers = list(f.read().strip().split(" "))

total = 0

table = {}

def blink(number, i, table):
    if i == 0:
        return 1
    if (number, i) in table:
        return table[(number, i)]
    
    count = 0
    
    digit_count = len(str(number))
    if number == 0:
        count += blink(1, i - 1, table)
    elif digit_count % 2 == 0:
        count += blink(int(str(number)[:digit_count//2]), i - 1, table)
        count += blink(int(str(number)[digit_count//2:]), i - 1, table)
    else:
        count += blink(number*2024, i - 1, table)

    table [(number, i)] = count

    return count

answer = 0
for number in numbers:
    answer += blink(int(number), 75, table)

print(answer)