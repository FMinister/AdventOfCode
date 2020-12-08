def read_file():
    instructions = []

    with open("Day_8_1.txt") as file:
        for line in file:
            instructions.append(line.replace("\n", "").strip())

    return instructions


def get_accumulator(instructions):
    accumulator = 0
    stop_indexes = []
    index = 0

    while index not in stop_indexes:
        stop_indexes.append(index)
        if "acc" in instructions[index]:
            accumulator = accumulator + int(instructions[index].replace("acc ", ""))
            index = index + 1
        elif "nop" in instructions[index]:
            index = index + 1
            pass
        else:
            index = index + int(instructions[index].replace("jmp ", ""))

    return accumulator


if __name__ == "__main__":
    instr = read_file()
    print(get_accumulator(instr))
