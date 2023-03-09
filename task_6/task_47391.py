from turtle import *
multiplier = 100
speed(500)
lt(90)
begin_fill()
for i in range(12): rt(60); fd(2*multiplier); rt(60); fd(2*multiplier); rt(270)
end_fill()
canvas = getcanvas()
print(sum([1 for x in range(-100*multiplier, 100*multiplier, multiplier) for y in range(-100*multiplier, 100*multiplier, multiplier) if len(canvas.find_overlapping(x, y, x, y)) == 1 and canvas.find_overlapping(x, y, x, y)[0] == 5]))
done()
