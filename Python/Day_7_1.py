def open_file(txt_file):
    bags_input = []
    with open(txt_file) as file:
        for line in file:
            line = line.replace("\n", "")
            bags_input.append(line)

    return bags_input


def get_colors(list_of_all_bags, list_of_bags_with_gold):
    for item in list_of_all_bags:
        items = item.split("contain")
        for bag in list_of_bags_with_gold:
            if bag in items[1]:
                color = items[0].replace("bags", "").replace("bag", "").strip()
                list_of_bags_with_gold.append(
                    color
                ) if color not in list_of_bags_with_gold else list_of_bags_with_gold

    return list_of_bags_with_gold


if __name__ == "__main__":
    list_of_all_bags = open_file("Day_7_1.txt")
    bags = ["shiny gold"]
    counter = 1
    while counter > 0:
        cache = len(bags)
        bags = get_colors(list_of_all_bags, bags)
        counter = len(bags) - cache
    print(len(bags) - 1)
