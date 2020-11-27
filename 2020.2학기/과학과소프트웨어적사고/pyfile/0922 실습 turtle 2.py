import turtle 
import math

t = turtle.Turtle()

# x 축 
t.forward(400)
t.penup()
t.goto(0,0)

t.left(180)
t.pendown()
t.forward(350)
t.penup()
t.goto(0,0)

# y축 
t.left(90)
t.pendown()
t.forward(350)
t.penup()
t.goto(0,0)

t.left(180)
t.pendown()
t.forward(350)
t.penup()
t.goto(-20,20)

t.pensize(3)
t.shape('turtle')

# Sine wave

for angle in range(361):
    t.pensize(3)
    t.pencolor('red')
    y = math.sin(math.radians(angle))
    scaledX = angle
    scaledY = y * 100
    t.goto(scaledX,scaledY)
    if angle in [ 90,180, 270,360]:
        t.pensize(1)
        t.pencolor('skyblue')
        t.goto(scaledX,0)
        t.write(angle)
        t.penup()
        t.goto(scaledX,scaledY)
        t.pendown()
    if angle in [0, 90,270]:
        t.pensize(1)
        t.pencolor('blue')
        t.goto(0,scaledY)
        t.penup()
        t.goto(-15,scaledY)
        t.write(scaledY/100)
        t.goto(scaledX,scaledY)
        t.pendown()
        
