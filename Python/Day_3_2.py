list = []

with open("Day_3_1.txt") as file:
    for line in file:
        list.append(line.replace("\n", ""))

print(list)

tree_counter = 0
index = 0

for line in list:
    if index < 31:
        object = line[index]
        index = index + 1
    else:
        index = index - 31
        object = line[index]
        index = index + 1
    if object == "#":
        tree_counter = tree_counter + 1

print(f"Part 1: {tree_counter}")

solution = tree_counter

tree_counter = 0
index = 0

for line in list:
    if index < 31:
        object = line[index]
        index = index + 3
    else:
        index = index - 31
        object = line[index]
        index = index + 3
    if object == "#":
        tree_counter = tree_counter + 1

print(f"Part 2: {tree_counter}")

solution = solution * tree_counter

tree_counter = 0
index = 0

for line in list:
    if index < 31:
        object = line[index]
        index = index + 5
    else:
        index = index - 31
        object = line[index]
        index = index + 5
    if object == "#":
        tree_counter = tree_counter + 1

print(f"Part 3: {tree_counter}")

solution = solution * tree_counter

tree_counter = 0
index = 0

for line in list:
    if index < 31:
        object = line[index]
        index = index + 7
    else:
        index = index - 31
        object = line[index]
        index = index + 7
    if object == "#":
        tree_counter = tree_counter + 1

print(f"Part 4: {tree_counter}")

solution = solution * tree_counter

tree_counter = 0
index = 0

list = list[::2]

print(list)

for line in list:
    if index < 31:
        object = line[index]
        index = index + 1
    else:
        index = index - 31
        object = line[index]
        index = index + 1
    if object == "#":
        tree_counter = tree_counter + 1

print(f"Part 5: {tree_counter}")

solution = solution * tree_counter

print(solution)