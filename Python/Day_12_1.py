instructions = []

with open("Day_12_1.txt") as file:
    for line in file:
        instructions.append(line.replace("\n", "").strip())

print(instructions)

position = (0, 0)
compass_directions = ["N", "E", "S", "W"]
index = 1
facing = compass_directions[index]

for instruction in instructions:
    if "R" in instruction:
        move = int(instruction.replace("R", ""))
        index = index + move / 90
        if index > 3:
            index = index - 4
        facing = compass_directions[int(index)]
    elif "L" in instruction:
        move = int(instruction.replace("L", ""))
        index = index - move / 90
        if index < 0:
            index = index + 4
        facing = compass_directions[int(index)]
    elif "N" in instruction:
        move = int(instruction.replace("N", ""))
        position = (position[0], position[1] + move)
    elif "E" in instruction:
        move = int(instruction.replace("E", ""))
        position = (position[0] + move, position[1])
    elif "S" in instruction:
        move = int(instruction.replace("S", ""))
        position = (position[0], position[1] - move)
    elif "W" in instruction:
        move = int(instruction.replace("W", ""))
        position = (position[0] - move, position[1])
    elif "F" in instruction:
        move = int(instruction.replace("F", ""))
        if facing == "E":
            position = (position[0] + move, position[1])
        elif facing == "W":
            position = (position[0] - move, position[1])
        elif facing == "N":
            position = (position[0], position[1] + move)
        elif facing == "S":
            position = (position[0], position[1] - move)


print(position)
print(position[0] - position[1])
