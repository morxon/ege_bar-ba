from itertools import permutations

print(len([res for res in [''.join(code) for code in permutations("ДЕМЬЯН")] if res[0] != "Ь" and res[res.index("Ь")-1]
           not in ['Я', 'Е']]))
