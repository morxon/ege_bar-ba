from turtle import *
k = 15
lt(90)
for _ in range(4): fd(7*k); rt(90); fd(8*k); rt(90)
pu()

for x in range(15):
    for y in range(15):
        goto(x*k, y*k)
        dot(5)
# 42
