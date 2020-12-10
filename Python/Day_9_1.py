import itertools

list = []

with open("Day_9_1.txt") as file:
    for line in file:
        list.append(int(line.replace("\n", "").strip()))

print(list)
counter = 25
while True:
    praemble = list[counter - 25 : counter]
    list_of_sums = []
    for numbers in itertools.combinations(praemble, 2):
        list_of_sums.append(sum(numbers))
    if list[counter] not in list_of_sums:
        print(list[counter])
        break
    counter = counter + 1
