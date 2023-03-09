from turtle import *
multiplier = 15
begin_fill()
for i in range(5): fd(8*multiplier); rt(60); fd(8*multiplier); rt(120)
end_fill()
canvas = getcanvas()
print(sum([1 for x in range(-100*multiplier, 100*multiplier, multiplier) for y in range(-100*multiplier, 100*multiplier, multiplier) if len(canvas.find_overlapping(x, y, x, y)) == 1 and canvas.find_overlapping(x, y, x, y)[0] == 5]))
done()

# fill 1/2 == 24
# answer 48