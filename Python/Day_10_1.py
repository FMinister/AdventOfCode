adapters = []

with open("Day_10_1.txt") as file:
    for line in file:
        adapters.append(int(line.replace("\n", "").strip()))

adapters.sort()

print(adapters)

one_jolt_adapters = []
three_jolt_adapters = []
index = 0

while index < len(adapters) - 1:
    if adapters[index] + 1 == adapters[index + 1]:
        one_jolt_adapters.append(adapters[index])
    else:
        three_jolt_adapters.append(adapters[index])
    index = index + 1

# +1 => starting at 0
one_jolt_adapter_steps = len(one_jolt_adapters) + 1
# +1 => ending at last number +3
three_jolt_adapter_steps = len(three_jolt_adapters) + 1

print(one_jolt_adapter_steps * three_jolt_adapter_steps)
