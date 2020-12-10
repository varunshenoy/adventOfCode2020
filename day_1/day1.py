f = open("input.txt", "r")

content = f.read().split()

for ind, c in enumerate(content):
    content[ind] = int(c)


for x in range(len(content)):
    valx = content[x]
    for y in range(x, len(content)):
        valy = content[y]
        for z in range(len(content)):
            if z == x or z == y:
                continue

            valz = content[z]
            if (valx + valy + valz == 2020):

                print(valx)
                print(valy)
                print(valz)
                print(valx * valy * valz)
