from copy import deepcopy
from math import prod

def categorize_parts(filepath):
    """ """

    with open(filepath, "r") as f: # open the file
        input_text = f.read().split("\n\n")
    
    workflows = {}
    for workflow in input_text[0].split("\n"):
        name = workflow[:workflow.index("{")]
        conditions = workflow[workflow.index("{")+1:workflow.index("}")].split(",")
        placeholder = []
        for condition in conditions:
            if ":" in condition:
                comparator, target = condition.split(":")
                placeholder.append(
                    {
                        "type": "comparison",
                        "target": target,
                        "variable": comparator[0],
                        "comparator": comparator[1],
                        "value": int(comparator[2:])
                    }
                )
            else:
                placeholder.append(
                    {
                        "type": "direct",
                        "target": condition
                    }
                )
        workflows[name] = placeholder

    count = 0
    uncategorized_parts = [{"x": [1, 4001], "m": [1, 4001], "a": [1, 4001], "s": [1, 4001], "rules": "in"}]
    while uncategorized_parts:
        part_range = uncategorized_parts.pop(0)
        sorting_piles = categorize_part_range(part_range, workflows)

        for piles in sorting_piles:
            if piles["rules"] == "A":
                count += prod([big-small for small, big in list(piles.values())[:-1]])
            elif piles["rules"] == "R":
                continue
            else:
                uncategorized_parts.append(piles)
    return count

def categorize_part_range(part_range, workflows):
    sorting_pile = []
    for instruction in workflows[part_range["rules"]]:
        if instruction["type"] == "comparison":
            if instruction["comparator"] == ">":
                if part_range[instruction["variable"]][1] > instruction["value"]:
                    new_pile = deepcopy(part_range)
                    new_pile[instruction["variable"]][0] = instruction["value"] + 1
                    new_pile["rules"] = instruction["target"]
                    sorting_pile.append(new_pile)
                    part_range[instruction["variable"]][1] = instruction["value"] + 1
            else:
                if part_range[instruction["variable"]][0] < instruction["value"]:
                    new_pile = deepcopy(part_range)
                    new_pile[instruction["variable"]][1] = instruction["value"]
                    new_pile["rules"] = instruction["target"]
                    sorting_pile.append(new_pile)
                    part_range[instruction["variable"]][0] = instruction["value"]
        else:
            part_range["rules"] = instruction["target"]
            sorting_pile.append(part_range)
    
    return sorting_pile

if __name__ == "__main__":  
    print(categorize_parts("input.txt"))