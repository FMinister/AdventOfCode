adapters = []

with open("Day_10_1.txt") as file:
    for line in file:
        adapters.append(int(line.replace("\n", "").strip()))

adapters.sort()

print(adapters)

adapters = [0] + adapters + [max(adapters) + 3]
possibilities = {adapters[0]:1}
for part in adapters[1:]:
    possibilities[part] = sum(possibilities[part - y] for y in range(1, 4) if part - y in possibilities)
print(possibilities[adapters[-1]])