part = ""
solution = 0
duplicates = ""

with open("Day_6_1.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        if line != "":
            if duplicates != "":
                duplicates = [
                    duplicate for duplicate in duplicates if duplicate in line
                ]
            else:
                duplicates = [letter for letter in line]
            part = part + line
        else:
            solution = solution + len(duplicates)
            duplicates = ""
            part = ""

print(solution)
