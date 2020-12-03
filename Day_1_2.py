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
        second = int(item)
        list2 = list[1:]
        for item in list2:
            third = int(item)
            if (current + second + third) == 2020:
                print(f"{current=}, {second=}, {third=}, result: {current * second * third}")