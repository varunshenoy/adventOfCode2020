def treeFinder(dy, dx, grid):
    current_row = 0
    current_col = 0

    trees = 0

    while current_row != len(grid) - 1:
        current_col = (current_col + dx) % (len(grid[0]))
        current_row += dy

        if grid[current_row][current_col] == '#':
            trees += 1

    return trees


f = open("input.txt", "r")

grid = f.read().split("\n")
grid.pop(len(grid) - 1)

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.


# cases
a = treeFinder(1, 1, grid)
b = treeFinder(1, 3, grid)
c = treeFinder(1, 5, grid)
d = treeFinder(1, 7, grid)
e = treeFinder(2, 1, grid)

print(a * b * c * d * e)
