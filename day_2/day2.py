# Part 1

f = open("input.txt", "r")

content = f.read().split()

total = 0

for i in range(int(len(content)/3)):
    nums = content[3 * i].split("-")
    charac = content[3 * i + 1][0]
    string = content[3 * i + 2]

    low = int(nums[0])
    hi = int(nums[1])

    char_count = 0
    for c in string:
        if c == charac:
            char_count += 1

    if (char_count >= low and char_count <= hi):
        total += 1

    print(((low, hi), charac, char_count, string))

print(total)

# Part 2

f = open("input.txt", "r")

content = f.read().split()

total = 0

for i in range(int(len(content)/3)):
    nums = content[3 * i].split("-")
    charac = content[3 * i + 1][0]
    string = content[3 * i + 2]

    ind1 = int(nums[0])
    ind2 = int(nums[1])

    if ((string[ind1 - 1] == charac or string[ind2 - 1] == charac) and (string[ind1 - 1] != string[ind2 - 1])):
        total += 1
        print((ind1, ind2), charac, string)
        print(string[ind1 - 1])
        print(string[ind2 - 1])

print(total)
