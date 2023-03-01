from itertools import product

print([''.join(code) for code in product("ВИНТ", repeat=5)][1019])
