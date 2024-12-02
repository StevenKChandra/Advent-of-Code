count = 0

def is_safe(num_list):
        increasing = num_list[0] - num_list[1]

        for i in range(len(num_list)-1):
            difference = num_list[i] - num_list[i+1]

            if increasing * difference < 0:
                return False
            
            if abs(difference) > 3 or abs(difference) < 1:
                return False

        return True
             
with open("2024/day 02/input.txt") as f:
    for line in f:
        num_list = list(map(int,line.split()))
        
        if is_safe(num_list):
            count += 1
    
print(count)