from sympy import symbols, Eq, solve

def find_rock_position(filepath):
    """ """

    with open(filepath, "r") as f: # open the file

        equations = []
        for line in f:
            line = line.rstrip().split(" @ ")
            
            position = [int(num) for num in line[0].split(", ")]
            velocity = [int(num) for num in line[1].split(", ")]

            equations.append(position+velocity)

    x0, x1, x2, x3, l0, l1 = symbols("x0, x1, x2, x3, l0, l1")
    eqs = [
        Eq(
            equations[2][i] - equations[0][i] + x2 * equations[2][i+3] - x0 * equations[0][i+3],
            l0 * ((equations[1][i] - equations[0][i]) + x1 * equations[1][i+3] - x0 * equations[0][i+3])
        )
        for i in range(3)
    ]

    eqs += [
        Eq(
            (equations[3][i] - equations[0][i]) + x3 * equations[3][i+3] - x0 * equations[0][i+3],
            l1 * ((equations[1][i] - equations[0][i]) + x1 * equations[1][i+3] - x0 * equations[0][i+3])
        )
        for i in range(3)
    ]

    solution = solve(eqs, [x0, x1, x2, x3, l0, l1])[0]
    
    rock_pos = [(solution[1]*(equations[0][i] + solution[0]*equations[0][i+3]) - solution[0]*(equations[1][i] + solution[1]*equations[1][i+3])) / (solution[1]-solution[0]) for i in range(3)]

    return sum(rock_pos)

if __name__ == "__main__":
    print(find_rock_position("input.txt"))