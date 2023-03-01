from itertools import product

print(len([code for code in product("1234", repeat=5) if code.count('1') == 2]))
