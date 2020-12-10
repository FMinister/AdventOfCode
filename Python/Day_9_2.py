import itertools

xmas_codes = []

with open("Day_9_1.txt") as file:
    for line in file:
        xmas_codes.append(int(line.replace("\n", "").strip()))

print(xmas_codes)
counter = 25
while True:
    praemble = xmas_codes[counter - 25 : counter]
    list_of_sums = []
    for numbers in itertools.combinations(praemble, 2):
        list_of_sums.append(sum(numbers))
    if xmas_codes[counter] not in list_of_sums:
        solution = xmas_codes[counter]
        index = xmas_codes.index(solution)
        break
    counter = counter + 1

counter = 2
c = 0
xmas_codes = xmas_codes[0:index]

while True:
    stop = ""
    for c in range(0, len(xmas_codes) - counter):
        praemble = xmas_codes[counter - counter + c : counter + c]
        list_of_sums = []
        for numbers in itertools.combinations(praemble, counter):
            list_of_sums.append(sum(numbers))
        if solution in list_of_sums:
            stop = 1
            praemble.sort()
            print(praemble[0] + praemble[-1])
            break
    counter = counter + 1
    if stop != "":
        break
