import math

with open("Day_12_1.txt", "r") as fp:
    lines = [(line.rstrip()[0], int(line.rstrip()[1:])) for line in fp.readlines()]


def rotate(origin, point, angle):
    # source: https://stackoverflow.com/a/34374437
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))


coord = {"x": 0, "y": 0}
waypoint = {"x": 10, "y": 1}
for line in lines:
    instruction, n = line
    if instruction == "N":
        waypoint["y"] += n
    elif instruction == "S":
        waypoint["y"] -= n
    elif instruction == "E":
        waypoint["x"] += n
    elif instruction == "W":
        waypoint["x"] -= n
    elif instruction == "F":
        coord["y"] += waypoint["y"] * n
        coord["x"] += waypoint["x"] * n
    elif instruction in ["L", "R"]:
        if instruction == "R":
            n = -n
        waypoint["x"], waypoint["y"] = rotate(
            (0, 0), (waypoint["x"], waypoint["y"]), math.radians(n)
        )
abs(coord["x"]) + abs(coord["y"])

print(coord)
print(coord["x"] - coord["y"])
