# Exercise 8
import turtle
import numpy as np

const_k = float(input("Enter k for ro = k * phi (for example, 20): "))
phi = np.arange(0, 360, 10)
turtle.shape('turtle')
screen = turtle.Screen()
screen.title("Turtle spiral")
turtle.color('green')
turtle.speed(4)

for i in phi:
    ro = const_k * ((i * np.pi) / 180)
    turtle.left(90)
    turtle.forward(ro)

    
turtle.down()