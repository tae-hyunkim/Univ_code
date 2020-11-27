import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.pensize(3)


x = -30
y = 30

t.penup()
t.goto(x,y)
t.pendown()

t.circle(100)

t.penup()
t.goto(x-60.62,y+65)
t.pendown()
t.setheading(-60)
t.circle(70,120)

t.penup()
t.goto(x-52,y+120)
t.dot(30)

t.goto(x+50,y+120)
t.dot(30)

