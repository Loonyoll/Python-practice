# Exercise 4
import turtle

turtle.shape('turtle')
while True:
    turtle.forward(10)
    turtle.left(5)
    if abs(turtle.pos() - (0, 0)) < 1:
        break
    
           