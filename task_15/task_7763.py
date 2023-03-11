# два отрезка: P = [5, 30] и Q = [14, 23].
P = [i for i in range(5, 31)]
Q = [i for i in range(14, 24)]
A_range = [A for A in range(-300, 300)]

for x in range(-300, 300):
    # ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)
    if not ((x in P) == (x in Q)) <= (not(x in A_range)):
        A_range.remove(x)

# before filter
print(A_range)
# after filter
res = [res for res in A_range if 5 <= res <= 14]  # where 5 is start of P, 14 is start of Q ((x ∈ P) ≡ (x ∈ Q))
print(res)
print(len(res))
# [5, 6, 7, 8, 9, 10, 11, 12, 13] - len 9
