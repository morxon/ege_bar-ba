from itertools import product

print("x y z w")
for x, y, z, w in product([0, 1], repeat=4):
    if ((x <= y) == (y <= z)) and (y or w):
        print(x, y, z, w)
