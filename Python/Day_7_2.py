import numpy as np


def main():
    with open("Day_7_1.txt", "r") as input_file:
        entries = input_file.read().split("\n")
    tuple_dict = {}
    color_to_id = {"shiny gold": 0}

    def get_id(color):
        try:
            color_id = color_to_id[color]
        except KeyError:
            color_id = len(color_to_id)
            color_to_id[color] = color_id
        return color_id

    for entry in entries:
        # Parsing stuff
        left_side, right_side = entry.split("contain")
        indexing_color = left_side.split("bags")[0][:-1]
        contained_bags = right_side.split(",")
        # code colors into matrix indices and add them to a dictionary for retrieval
        tuples_contained = []
        if not contained_bags[0] == " no other bags.":
            for bag in contained_bags:
                tuples_contained.append(
                    (get_id(bag.split("bag")[0][3:-1]), int(bag[1]))
                )
        tuple_dict[get_id(indexing_color)] = tuples_contained
    # transfer values to numpy matrix
    bag_matrix = np.zeros((len(color_to_id), len(color_to_id)))
    for key, value in tuple_dict.items():
        for contained_tuple in value:
            bag_matrix[key, contained_tuple[0]] = contained_tuple[1]
    # Solve
    mul_matrix = bag_matrix.copy()
    aux_matrix = bag_matrix.copy()
    while True:
        mul_matrix = mul_matrix.dot(aux_matrix)
        bag_matrix += mul_matrix
        if np.all((mul_matrix == 0)):
            break
    return bag_matrix, color_to_id


final_matrix, color_dict = main()
print(np.count_nonzero(final_matrix[:, color_dict["shiny gold"]]))
print(np.sum(final_matrix[color_dict["shiny gold"], :]))
