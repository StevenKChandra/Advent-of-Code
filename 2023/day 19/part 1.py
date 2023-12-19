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

    A = []
    R = []
    for part in input_text[1].split("\n"):
        if not part:
            continue
        placeholder = {}
        for char in part[1:-1].split(","):
            placeholder[char.split("=")[0]] = int(char.split("=")[1])
        categorize_part(placeholder, "in", workflows, A, R)
    
    return sum([sum([char for char in part.values()]) for part in A])

def categorize_part(part, key, workflows, accept_pile, reject_pile):
    if key == "A":
        accept_pile.append(part)
        return
    if key == "R":
        reject_pile.append(part)
        return
    for instruction in workflows[key]:
        if instruction["type"] == "comparison":
            if instruction["comparator"] == ">":
                if part[instruction["variable"]] > instruction["value"]:
                    categorize_part(part, instruction["target"], workflows, accept_pile, reject_pile)
                    return
            else:
                if part[instruction["variable"]] < instruction["value"]:
                    categorize_part(part, instruction["target"], workflows, accept_pile, reject_pile)
                    return
        else:
            categorize_part(part, instruction["target"], workflows, accept_pile, reject_pile)

if __name__ == "__main__":  
    print(categorize_parts("input.txt"))