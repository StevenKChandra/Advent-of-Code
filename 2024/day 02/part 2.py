count = 0

def is_safe(num_list):
        increasing = num_list[0] - num_list[1]

        for i in range(len(num_list)-1):
            difference = num_list[i] - num_list[i+1]

            if increasing * difference < 0:
                return (i, False)
            
            if abs(difference) > 3 or abs(difference) < 1:
                return (i, False)

        return (-1, True)
             
with open("2024/day 02/input.txt") as f:
    for line in f:
        num_list = list(map(int,line.split()))
        
        i, safe = is_safe(num_list)

        if safe:
            count += 1
            continue

        list_copy = num_list.copy()
        del list_copy[i]

        j, safe = is_safe(list_copy)

        if safe:
            count += 1
            continue
        
        list_copy = num_list.copy()
        del list_copy[i+1]

        j, safe = is_safe(list_copy)

        if safe:
            count += 1
            continue

        list_copy = num_list.copy()
        del list_copy[0]

        j, safe = is_safe(list_copy)

        if safe:
            count += 1
            continue
        
print(count)