import turtle

turtle.shape('turtle')
turtle.color('green')
turtle.speed(0)
turtle.left(90)

X = range(0, 180, 1)

def spring(radius:int):
    for i in range(0, 5, 1):
        for i in X:
            turtle.forward(radius / 30)
            turtle.right(1)
        for i in X:
            turtle.forward(radius / 200)
            turtle.right(1)
       
spring(30)
turtle.down()
        