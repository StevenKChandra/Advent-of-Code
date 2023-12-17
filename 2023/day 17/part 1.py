from queue import PriorityQueue

def find_shortest_path(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        
        map = [[int(num) for num in row.rstrip()] for row in f]

    NUM_ROW = len(map)
    NUM_COL = len(map[0])

    destination = (NUM_ROW-1, NUM_COL-1)

    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    hottest_vertices = PriorityQueue()
    hottest_vertices.put((0, (0,0), 0, 0))
    hottest_vertices.put((0, (0,0), 0, 1))
    
    def add_to_queue(position, direction_length, direction):
        row = position[0] + directions[direction][0]
        col = position[1] + directions[direction][1]
        if row < 0 or NUM_ROW <= row or col < 0 or NUM_COL <= col:
            return
        hottest_vertices.put((heat_loss + map[row][col], (row,col), direction_length, direction))
    
    visited_vertices = {}

    i = 0
    while hottest_vertices:
        heat_loss, position, direction_length, direction = hottest_vertices.get()

        if i % 1717 == 0:
            4
        if position == destination:
            return heat_loss

        if (position, direction_length, direction) in visited_vertices:
            continue

        visited_vertices[(position, direction_length, direction)] = heat_loss

        if direction_length < 3:
            add_to_queue(position, direction_length+1, direction)
        
        add_to_queue(position, 1, (direction+1)%4)
        add_to_queue(position, 1, (direction-1)%4)

        i += 1
    
if __name__ == "__main__":
    print(find_shortest_path("input.txt"))