from itertools import permutations

print(len([code for code in [''.join(code) for code in permutations("ЛЕВИЙ")] if code[0] != "Й" and "ЕИ" not in code]))
