import turtle

t = turtle.Turtle()

#grass below
t.goto(-350,0)
t.color("green")

t.right (90)
t.goto(350,0)
t.penup()
t.goto(200,250)
t.pendown()

#moon below
t.color("yellow")

for i in range(50):
    t.left(20)
    t.forward(30)

for i in range(50):
    t.forward(10 -1)
    t.left(5)


#bush below
t.penup()
t.goto(-200,-50)
t.pendown()
t.color("green")

for i in range(50):
    t.forward(5 +1)
    t.left(5)

t.goto(-150,-50)

for i in range(100):
    t.forward(5 +1)
    t.left(5)

t.penup()
t.goto(-100,-50)
t.pendown()

for i in range(100):
    t.forward(5 +1)
    t.left(5)

t.goto(-140,-50)

for i in range(100):
    t.forward(5 +1)
    t.left(5)

turtle.exitonclick ()