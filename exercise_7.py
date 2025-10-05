# Exercise 7
import turtle
import numpy as np

const_k = float(input("Enter k for ro = k * phi (for example, 3): "))
phi = np.arange(0, 720, 1)
turtle.shape('turtle')
screen = turtle.Screen()
screen.title("Turtle spiral")
turtle.color('green')
turtle.speed(0)

for i in phi:
    ro = const_k * ((i * np.pi) / 180)
    turtle.left(8)
    turtle.forward(ro)

    
turtle.down()