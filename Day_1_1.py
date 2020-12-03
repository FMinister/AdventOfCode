list = []

with open("Day_1_1.txt") as file:
    for line in file:
        list.append(line.replace("\n", ""))

result = 0

#while result != 2020:
for item in list:
    current = int(item)
    list = list[1:]
    for item in list:
        item = int(item)
        if (current + item) == 2020:
            print(f"{current=}, {item=}, result: {current * item}")