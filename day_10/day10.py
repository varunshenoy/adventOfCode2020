from functools import lru_cache


def part1(adapters):

    ones = 0
    threes = 0

    for i in range(len(adapters) - 1):
        if adapters[i + 1] - adapters[i] == 1:
            ones += 1
        elif adapters[i + 1] - adapters[i] == 3:
            threes += 1

    return ones * threes


def part2(adapters):
    dp = [0]*len(adapters)

    dp[0] = 1
    dp[1] = 1

    if adapters[2] - adapters[0] <= 3:
        dp[2] = 2
    else:
        dp[2] = 1

    for i in range(3, len(adapters)):
        for j in range(1, 4):
            if adapters[i] - adapters[i-j] <= 3:
                dp[i] += dp[i-j]

    return dp[-1]


def main():
    f = open("input.txt", "r")
    my_adapters = [int(x) for x in f.read().strip().split("\n")]

    my_adapters.append(0)
    my_adapters.append(max(my_adapters) + 3)

    my_adapters.sort()

    sol = part1(my_adapters)
    print(sol)

    sol = part2(my_adapters)
    print(sol)


if __name__ == "__main__":
    main()
