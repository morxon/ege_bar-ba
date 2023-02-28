from turtle import *
left(90)
for i in range(5):
    forward(7*30)
    right(90)
    forward(4*30)
    right(90)
pu()
for x in range(8):
    for y in range(8):
        goto(x*30, y*30)
        dot(5)
done()
