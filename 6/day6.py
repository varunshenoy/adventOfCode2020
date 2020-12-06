def numberOfYes(group):

    # PART 2
    total = 0
    for question in group[0]:
        search = 1
        for passenger in group[1:]:
            if question in passenger:
                search += 1
        if search == len(group):
            total += 1
    return total

    # PART 1
    yeses = set()
    for passenger in group:
        for question in passenger:
            yeses.add(question)

    return len(yeses)


def main():
    f = open("input.txt", "r")

    data = [x.split() for x in f.read().split("\n\n")]

    total = 0
    for group in data:
        total += numberOfYes(group)
    print(total)


if __name__ == "__main__":
    main()
