def day11_1():
    with open("Day_11_1.txt", "r") as file:
        data = file.read()
    data = data.split("\n")

    old_layout = {}
    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            old_layout[i, j] = seat

    layout = {}
    while True:
        for (row, col), seat in old_layout.items():
            if seat == ".":
                layout[row, col] = "."
            elif seat == "L":
                neighbors = ""
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == j == 0:
                            continue
                        neighbors += old_layout.get((row - i, col - j), ".")
                occupied = neighbors.count("#")

                if not occupied:
                    layout[row, col] = "#"

            elif seat == "#":
                neighbors = ""
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == j == 0:
                            continue
                        neighbors += old_layout.get((row - i, col - j), ".")
                occupied = neighbors.count("#")

                if occupied >= 4:
                    layout[row, col] = "L"

        if layout == old_layout:
            break
        old_layout = {key: value for key, value in layout.items()}

    count = 0
    for v in layout.values():
        if v == "#":
            count += 1

    return count


if __name__ == "__main__":
    print(day11_1())
