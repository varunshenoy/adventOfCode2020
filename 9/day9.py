def isValidNext(window, next_num):
    for x in window:
        for y in window:
            if x + y == next_num:
                return True
    return False


def part1(data, preable_size):
    window = []
    for preable_num in data[:preable_size]:
        window.append(preable_num)

    for next_input in data[preable_size:]:
        if not isValidNext(window, next_input):
            return next_input
        else:
            window.pop(0)
            window.append(next_input)
    return -1


def part2(data, value_to_find):
    for ind, initial in enumerate(data):
        net_sum = initial
        net_subarr = [initial]
        for tail in data[ind + 1:]:
            net_sum += tail
            net_subarr.append(tail)
            if net_sum == value_to_find:
                return (min(net_subarr) + max(net_subarr), initial, tail)
    return -1


def main():
    f = open("input.txt", "r")
    data = [int(x) for x in f.read().strip().split("\n")]

    part1_sol = part1(data, 25)
    print(part1_sol)
    print(part2(data, part1_sol))


if __name__ == "__main__":
    main()
