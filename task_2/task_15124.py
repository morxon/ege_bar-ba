from itertools import product

print("x y z")
for x, y, z in product([0, 1], repeat=3):
    if not((x == y) or ((y or z) <= x)):
        print(x, y, z)
