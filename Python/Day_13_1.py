arrival = 0
busses = []
lines = []

with open("Day_13_1.txt", "r") as file:
    for line in file:
        lines.append(line.strip().rstrip("\n"))

print(lines)

arrival = int(lines[0])
busses = [int(bus) for bus in lines[1].split(",") if bus != "x"]
print(busses)

bus_departures = []
for bus in busses:
    departure = 0
    bus_departure = {"bus": "", "departure": ""}
    while departure < arrival:
        departure = departure + bus
    bus_departure["bus"] = bus
    bus_departure["departure"] = departure
    bus_departures.append(bus_departure)

print(bus_departures)

cache = (0, 10000000)

for bus in bus_departures:
    if bus["departure"] - arrival < cache[1]:
        cache = (bus["bus"], bus["departure"] - arrival)

print(cache)
print(cache[0] * cache[1])