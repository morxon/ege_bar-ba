for a in range(0, 1000):
    len_pair = 0
    for x in range(0, 1000):
        # x&25 ≠ 0 → (x&17 = 0 → x&А ≠ 0)
        if (x & 25 != 0) <= ((x & 17 == 0) <= (x & a != 0)):
            len_pair += 1
    if len_pair == 1000:  # 1000 x
        print(a)
        break
