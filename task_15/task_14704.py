A_count = 0
for A in range(1, 300):
    pair_count = 0
    for x in range(0, 300):
        for y in range(0, 300):
            # ((x < 6) → (x2 < A)) ∧ ((y2 ≤ A) → (y ≤ 6))
            if ((x < 6) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 6)):
                pair_count += 1
    if pair_count == 90_000:  # 300*300, all x and y
        A_count += 1
print(A_count)
