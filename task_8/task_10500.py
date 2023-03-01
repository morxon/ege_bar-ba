from itertools import product

print(len([code for code in product("12345", repeat=5) if code.count('1') == 3]))
