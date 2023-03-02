from itertools import product

print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if not ((x <= y) and (y <= w) or (z == (x or y))):
        print(x, y, z, w)
# 1-x 2-w 3-z 4 -y
# xwzy
