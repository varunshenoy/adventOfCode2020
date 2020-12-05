def binaryFind(data, low, hi, lowerHalfChar="F", upperHalfChar="B"):
    med = int((low + hi) / 2)
    if low == hi:
        return low
    elif data[0] == lowerHalfChar:
        return binaryFind(data[1:], low, med, lowerHalfChar=lowerHalfChar, upperHalfChar=upperHalfChar)
    elif data[0] == upperHalfChar:
        return binaryFind(data[1:], med + 1, hi, lowerHalfChar=lowerHalfChar, upperHalfChar=upperHalfChar)


def findSeatID(seat):
    r = binaryFind(seat[:7], 0, 127)
    c = binaryFind(seat[7:], 0, 7, lowerHalfChar="L", upperHalfChar="R")
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

    print(findMyID(IDs))


if __name__ == "__main__":
    main()
