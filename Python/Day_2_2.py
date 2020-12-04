list = []

with open("Day_2_1.txt") as file:
    for line in file:
        list.append(line.replace("\n", ""))

print(list)

valid_password_counter = 0

for item in list:
    items = item.split(":")
    password = items[1].strip()
    char = items[0].split(" ")[1]
    number1 = int(items[0].split("-")[0]) - 1
    number2 = int(items[0].split("-")[1].split(" ")[0]) - 1
    counter = 0
    if password[number1] == char and password[number2] != char or password[number1] != char and password[number2] == char:
        print(f"{number1=}, {number2=}, {char=}, {password=}")
        valid_password_counter = valid_password_counter + 1

print(valid_password_counter)