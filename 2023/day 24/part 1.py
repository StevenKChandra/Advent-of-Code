def count_intersections(filepath):
    """ """

    with open(filepath, "r") as f: # open the file

        equations = []
        for line in f:
            line = line.rstrip().split(" @ ")
            
            position = [int(num) for num in line[0].split(", ")]
            velocity = [int(num) for num in line[1].split(", ")]

            equations.append(
                {
                    "gradient": velocity[1]/velocity[0],
                    "constant": position[1] - velocity[1]/velocity[0]*position[0],
                    "time data": (position[0], velocity[0])
                }
            )

    count_intersections = 0
    for i, first_equation in enumerate(equations):
        for second_equation in equations[i+1:]:
            if first_equation["gradient"] == second_equation["gradient"]: continue
            x_intercept = -1 * (second_equation["constant"] - first_equation["constant"]) / (second_equation["gradient"] - first_equation["gradient"])
            if (x_intercept - first_equation["time data"][0]) / first_equation["time data"][1] < 0: continue
            if (x_intercept - second_equation["time data"][0]) / second_equation["time data"][1] < 0: continue
            if x_intercept < LIMIT[0] or x_intercept > LIMIT[1]: continue
            y_intercept = first_equation["gradient"] * x_intercept + first_equation["constant"]
            if y_intercept < LIMIT[0] or y_intercept > LIMIT[1]: continue
            count_intersections += 1
    return count_intersections


if __name__ == "__main__":
    LIMIT = (200000000000000, 400000000000000)
    print(count_intersections("input.txt"))