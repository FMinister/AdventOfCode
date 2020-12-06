part = ""
solution = 0

with open("Day_6_1.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        if line != "":
            part = part + line
        else:
            solution = solution + len("".join(set(part)))
            part = ""

print(solution)
