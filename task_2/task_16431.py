from itertools import product

print("x y z w")
for x, y, z, w in product([0, 1], repeat=4):
    if ((y <= x) == (x <= w)) and (z or x):
        print(x, y, z, w)


# x -
# y - 2
# z - 4
# w -
