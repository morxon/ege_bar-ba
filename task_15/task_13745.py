for A in range(300, 1, -1):
    pair_count = 0
    for x in range(0, 300):
        for y in range(0, 300):
            # ((x ≤ 9) →(x ⋅ x ≤ A)) ⋀ ((y ⋅ y ≤ A) → (y ≤ 9))
            if ((x <= 9) <= (x*x <= A)) and (((y*y <= A) <= (y <= 9))):
                pair_count += 1
    if pair_count == 90_000:  # 300*300, all x and y
        print(A)
        break
