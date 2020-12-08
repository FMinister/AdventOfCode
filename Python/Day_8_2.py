def read_file():
    instructions = []

    with open("Day_8_1.txt") as file:
        for line in file:
            instructions.append(line.replace("\n", "").strip())

    return instructions


def get_accumulator_and_index(instructions):
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
        elif "jmp" in instructions[index]:
            index = index + int(instructions[index].replace("jmp ", ""))
        else:
            return accumulator, index

    return accumulator, stop_indexes


def change_instructions(instructions, stop_indexes):
    for index in reversed(stop_indexes):
        if "jmp" in instructions[index]:
            changed_instructions = instructions
            changed_instructions[index] = instructions[index].replace("jmp", "nop")
            accumulator, stop_index = get_accumulator_and_index(changed_instructions)
        elif "nop" in instructions[index]:
            changed_instructions = instructions
            changed_instructions[index] = instructions[index].replace("nop", "jmp")
            accumulator, stop_index = get_accumulator_and_index(changed_instructions)
        else:
            pass

        if stop_index == len(instructions) - 1:
            return accumulator


if __name__ == "__main__":
    instr = read_file()
    accu, indexes = get_accumulator_and_index(instr)
    print(change_instructions(instr, indexes))
