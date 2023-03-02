from itertools import product

print("x y z w")
for w, x, y, z in product([0, 1], repeat=4):
    if not ((x and not (y)) or (y == z) or not(w)):
        print(x, y, z, w)

