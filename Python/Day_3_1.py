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
        index = index + 3
    else:
        index = index - 31
        object = line[index]
        index = index + 3
    if object == "#":
        tree_counter = tree_counter + 1

print(tree_counter)