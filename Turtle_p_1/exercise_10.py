import turtle 

turtle.shape('turtle')
turtle.color('green')
turtle.speed(0)
X = range(0, 360, 1)

def draw_circle(circle_radius):
    
    for i in X:
        turtle.forward(circle_radius / 10)
        turtle.left(5)
        if abs(turtle.pos() - (0, 0)) < 0.01:
            break
    turtle.left(60)
    
    for i in X:
        turtle.forward(circle_radius / 10)
        turtle.left(5)
        if abs(turtle.pos() - (0, 0)) < 0.01:
            break
    turtle.left(60)
    for i in X:
        turtle.forward(circle_radius / 10)
        turtle.left(5)
        if abs(turtle.pos() - (0, 0)) < 0.01:
            break
    turtle.left(60)
    for i in X:
        turtle.forward(circle_radius / 10)
        turtle.left(5)
        if abs(turtle.pos() - (0, 0)) < 0.01:
            break
    turtle.left(60)
    
    for i in X:
        turtle.forward(circle_radius / 10)
        turtle.left(5)
        if abs(turtle.pos() - (0, 0)) < 0.01:
            break
    turtle.left(60)
    for i in X:
        turtle.forward(circle_radius / 10)
        turtle.left(5)
        if abs(turtle.pos() - (0, 0)) < 0.01:
            break
              
draw_circle(35)

turtle.down()