def open_file():
    with open("Day_13_1.txt", "r") as fp:
        lines = fp.readlines()
    busses = ["x" if x == "x" else int(x) for x in lines[1].split(",")]

    return busses


def part2(busses):
    # index, bus in busses, -i % bus: departure-difference to index
    bus_line_departures = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
    bus_values = list(reversed(sorted(bus_line_departures)))
    departure = bus_line_departures[bus_values[0]]
    timestamp = bus_values[0]
    for bus in bus_values[1:]:
        while departure % bus != bus_line_departures[bus]:
            departure = departure + timestamp
        timestamp = timestamp * bus

    return departure


if __name__ == "__main__":
    input = open_file()
    print(part2(input))
