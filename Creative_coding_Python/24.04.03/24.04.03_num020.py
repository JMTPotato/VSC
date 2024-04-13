import turtle
t = turtle.Turtle()
t.shape('turtle')

xPoint = 0
yPoint = 0

for i in range(1, 6):
    for j in range(0, i):
        t.circle(20)
        
        t.up()
        xPoint += 50
        t.goto(xPoint, yPoint)
        t.down()
        
    xPoint = 0
    yPoint -= 50
    
    t.up()
    t.goto(xPoint, yPoint)
    t.down()