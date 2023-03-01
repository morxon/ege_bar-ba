from itertools import product

print([code for code in product("ВЕСТ", repeat=6)].index(
    [code for code in product("ВЕСТ", repeat=6) if code[0] == "Т"][0]) + 1)
