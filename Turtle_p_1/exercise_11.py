import turtle

turtle.shape('turtle')
turtle.color('green')
turtle.speed(0)

X = range(0, 360, 1)

def draw_butterfly(r_s:int):
    turtle.left(90)
    for i in range(0, 10, 1):
        for i in X:
            turtle.forward(r_s / 10)
            turtle.left(5)
            if abs(turtle.pos() - (0, 0)) < 0.01:
                break
    
        for i in X:
            turtle.forward(r_s / 10)
            turtle.right(5)
            if abs(turtle.pos() - (0, 0)) < 0.01:
                r_s += 7
                break
            

draw_butterfly(30)
turtle.down()