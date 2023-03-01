from itertools import product

print(len([code for code in product("ТИМОФЕЙ", repeat=5) if code.count('Й') >= 1 >= code.count("Т")]))
