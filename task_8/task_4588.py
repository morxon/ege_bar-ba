from itertools import product

print([code for code in [''.join(code) for code in product("АМУХ", repeat=4)]].index("ХУХХ") + 1)
