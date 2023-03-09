from turtle import *
speed(500)
lt(90)
k = 30
for i in range(6): fd(13*k); rt(120)

pu()
for x in range(30):
    for y in range(30):
        goto(x*k, y*k)
        dot(5)
done()

#66
