import turtle

turtle.shape('turtle')
turtle.color('green')

# Angle = 180 - (180/n)
def print_star():
    for i in range(0, 5, 1):
        turtle.forward(100)
        turtle.right(144)
        if abs(turtle.pos() - (0, 0)) < 0.01:
            break
    turtle.penup()
    turtle.goto(200, 0)
    turtle.pendown()
    for i in range(0, 11, 1):
        turtle.forward(100)
        turtle.right(163.636)
        if abs(turtle.pos() - (0, 0)) < 0.001:
            break
        
print_star()

turtle.mainloop()