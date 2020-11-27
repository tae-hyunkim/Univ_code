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
t.goto(0,0)

t.pensize(3)
t.shape('turtle')

# Sine wave
t.pencolor('red')
t.pendown()

for angle in range(720):
    y = math.sin(math.radians(angle))
    scaledX = angle
    scaledY = y * 100
    t.goto(scaledX,scaledY)

t.penup()

t.goto(0,100)
t.pencolor('blue')
t.pendown()
for angle in range(720):
    y = math.cos(math.radians(angle))
    scaledX = angle
    scaledY = y * 100
    print(scaledY)
    t.goto(scaledX,scaledY)
