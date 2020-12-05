def binaryFind(data, lowerHalfChar, upperHalfChar):
    data = data.replace(lowerHalfChar, "0").replace(upperHalfChar, "1")
    return int(data, 2)


def findSeatID(seat):
    r = binaryFind(seat[:7], "F", "B")
    c = binaryFind(seat[7:], "L", "R")
    return r * 8 + c


def findMyID(seatIDs):

    # no point in doing binary search since the list is so small lol
    seatIDs.sort()
    for i in range(len(seatIDs) - 2):
        thisSeat = seatIDs[i]
        nextSeat = seatIDs[i + 1]
        if thisSeat != nextSeat - 1:
            return thisSeat + 1
    return


def main():
    f = open("input.txt", "r")

    data = f.read().split("\n")

    IDs = []

    for seat in data:
        if seat == "":
            continue
        IDs.append(findSeatID(seat))

    # Part 1
    print(max(IDs))

    # Part 2
    print(findMyID(IDs))


if __name__ == "__main__":
    main()
