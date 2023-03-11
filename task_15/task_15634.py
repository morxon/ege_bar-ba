for A in range(1, 300):
    pair_count = 0
    for x in range(0, 300):
        for y in range(0, 300):
            # (y + 2x < A) ∨ (x > 30) ∨ (y > 20)
            if (y + 2*x < A) or (x > 30) or (y > 20):
                pair_count += 1
    if pair_count == 90_000:  # 300*300, all x and y
        print(A)
        break
