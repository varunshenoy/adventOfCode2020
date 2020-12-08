def hasInfiniteLoop(data):
    visited_indices = set()
    accumulated = 0
    counter = 0

    while True:
        # reached end of program
        if counter == len(data) - 1:
            return (False, accumulated)

        instruction = data[counter]

        # we have an infinite loop iff we go to an already processed line
        if counter in visited_indices:
            return (True, accumulated)
        elif instruction[0] == "acc":
            accumulated += int(instruction[1])
        elif instruction[0] == "jmp":
            counter += int(instruction[1])
            continue

        visited_indices.add(counter)
        counter += 1


def findWrongInstr(data):
    for ind, instr in enumerate(data):
        if instr[0] == "jmp" or instr[0] == "nop":
            data_cp = data.copy()
            new_instr = "nop" if instr[0] == "jmp" else "jmp"
            data_cp[ind] = [new_instr, data[ind][1]]

            test = hasInfiniteLoop(data_cp)
            if not test[0]:
                return test[1]


def main():
    f = open("input.txt", "r")
    data = [x.strip().split() for x in f.read().strip().split("\n")]

    # Part 1
    print(hasInfiniteLoop(data)[1])

    # Part 2
    print(findWrongInstr(data))


if __name__ == "__main__":
    main()
