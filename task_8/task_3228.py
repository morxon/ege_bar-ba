from itertools import product

print([''.join(code) for code in product('АОУ', repeat=5)].index("УАУАУ") + 1)
