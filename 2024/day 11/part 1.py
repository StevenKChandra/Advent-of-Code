with open("2024/day 11/input.txt") as f:
    numbers = list(f.read().strip().split(" "))

total = 0

table = {}

def blink(number, i, table):
    if i == 0:
        return [number]
    if (number, i) in table:
        return table[(number, i)]
    
    answer = []
    
    digit_count = len(str(number))
    if number == 0:
        answer += blink(1, i - 1, table)
    elif digit_count % 2 == 0:
        answer += blink(int(str(number)[:digit_count//2]), i - 1, table)
        answer += blink(int(str(number)[digit_count//2:]), i - 1, table)
    else:
        answer += blink(number*2024, i - 1, table)

    table [(number, i)] = answer

    return answer

answer = []
for number in numbers:
    answer += blink(int(number), 25, table)

print(len(answer))