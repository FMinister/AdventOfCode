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
    number1 = items[0].split("-")[0]
    number2 = items[0].split("-")[1].split(" ")[0]
    counter = 0
    for c in password:
        if c == char:
            counter = counter + 1
    if int(number1) <= counter <= int(number2):
        print(f"{number1=}, {number2=}, {counter=}, {char=}, {password=}")
        valid_password_counter = valid_password_counter + 1


print(valid_password_counter)