range_list = [A for A in range(-300, 300)]

for x in range(-300, 300):
    # ((x ∈ A) → (x2 ≤ 100)) ∧ ((x2 ≤ 64) → (x ∈ A))
    if not ((x in range_list) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in range_list)):
        range_list.remove(x)

print(range_list)  # [-10, -9, ... 8, 9, 10] - 20
