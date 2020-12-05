list = []

with open("Day_5_1.txt") as file:
    for line in file:
        line = (
            line.replace("\n", "")
            .strip()
            .replace("F", "0")
            .replace("B", "1")
            .replace("R", "1")
            .replace("L", "0")
        )
        list.append((line[:7], line[7:]))

seat_numbers = []

for item in list:
    seat_number = int(item[0], 2) * 8 + int(item[1], 2)
    seat_numbers.append(seat_number)

seat_numbers = sorted(seat_numbers)

missing_seats = [
    seat for seat in range(max(seat_numbers) + 1) if seat not in seat_numbers
]

for index, item in enumerate(missing_seats[1:]):
    if missing_seats[index] + 1 < (item):
        print(item)
