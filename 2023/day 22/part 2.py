def count_garden_plot(filepath):
    """ """

    with open(filepath, "r") as f: # open the file

        bricks_arrangement = [[[None for x in range(10)] for y in range(10)] for z in range(400)]
        table = []

        block_number = 0
        for line in f:

            start, end = line.rstrip().split("~")
            start, end = start.split(","), end.split(",")

            for z in range(int(start[2])-1, int(end[2])):
                for y in range(int(start[1]), int(end[1])+1):
                    for x in range(int(start[0]), int(end[0])+1):
                        bricks_arrangement[z][y][x] = block_number
            
            table.append(((int(start[2])-1, int(end[2])), (int(start[1]), int(end[1])+1), (int(start[0]), int(end[0])+1), block_number))
            
            block_number += 1

    table.sort()

    dependence = {key: [] for key in range(len(table))}
    for index, item in enumerate(table):
        x_start, x_end = item[2]
        y_start, y_end = item[1]
        z_start, z_end = item[0]
        block_number = item[3]
        
        steps_down = 0
        cont = True
        for z in range(z_start, z_end):
                for y in range(y_start, y_end):
                    for x in range(x_start, x_end):
                        bricks_arrangement[z][y][x] = None
        
        while cont and z_start-steps_down > 0:
            cont = all([all([bricks_arrangement[z_start-steps_down-1][y][x] == None for x in range(x_start, x_end)]) for y in range(y_start, y_end)])
            if cont:
                steps_down += 1
            else:
                dependence[block_number] = list(set([bricks_arrangement[z_start-steps_down-1][y][x] for x in range(x_start, x_end) for y in range(y_start, y_end) if bricks_arrangement[z_start-steps_down-1][y][x] != None]))
        
        for z in range(z_start-steps_down, z_end-steps_down):
                for y in range(y_start, y_end):
                    for x in range(x_start, x_end):
                        bricks_arrangement[z][y][x] = block_number
        
        table[index] = ((z_start-steps_down, z_end-steps_down), (y_start, y_end), (x_start, x_end), block_number)

    cannot_be_disintegrated = []
    for bricks in dependence.values():
        if len(bricks) == 1 and bricks[0] not in cannot_be_disintegrated:
            cannot_be_disintegrated.append(bricks[0])
    
    total_count = 0
    for i in range(len(table)):
        moved_bricks = [i]
        count = 0
        while len(moved_bricks) != count:
            count = len(moved_bricks)
            for key, bricks in dependence.items():
                if bricks != [] and all([brick in moved_bricks for brick in bricks]) and key not in moved_bricks:
                    moved_bricks.append(key)
        total_count += count - 1

    return total_count

if __name__ == "__main__":  
    print(count_garden_plot("input.txt"))