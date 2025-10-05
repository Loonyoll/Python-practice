import turtle

turtle.shape('turtle')
turtle.speed(0)

X = range(0, 360, 1)
Y = range(0, 180, 1)
turtle.penspeed(0)

def turtle_circle(radius:int):
    for i in X:
        turtle.forward(radius / 100)
        turtle.left(1)

def smile_face(radius:int):
    turtle.left(90)
    turtle.pencolor('yellow')
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle_circle(radius)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-113, 40)
    turtle.pendown()
    turtle.pencolor('blue')
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle_circle(radius/7)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(-30, 40)
    turtle.pendown()
    turtle.pencolor('blue')
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle_circle(radius/7)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(-90, 15)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('black')
    turtle.begin_fill()
    for i in Y:
        turtle.forward(radius / 1200)
        turtle.right(1)
    turtle.forward(45)
    for i in Y:
        turtle.forward(radius / 1200)
        turtle.right(1)
    turtle.forward(45)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(-117, -30)
    turtle.pendown()
    turtle.right(180)
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in Y:
        turtle.forward(radius / 250)
        turtle.left(1)
    for i in Y:
        turtle.forward(radius / 1500)
        turtle.right(1)
    for i in Y:
        turtle.forward(radius / 187)
        turtle.right(1)
    for i in Y:
        turtle.forward(radius / 1500)
        turtle.right(1)
    turtle.end_fill()
    
smile_face(150)

turtle.hideturtle()

turtle.mainloop()

