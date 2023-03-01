from itertools import product

print(len([code for code in product("ВИШНЯ", repeat=6) if code.count('В') <= 1 and (code[0] != "Ш" and code[5]
                                                                                    not in ['И', 'Я'])]))
