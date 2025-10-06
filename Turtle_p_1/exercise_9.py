# Exercise 9
import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(2)
r_const = 25
margin = 10

def regular_polygon(number_of_sides:int, radius_of_circle:float):
    global margin
    alpha = (360.0 / number_of_sides) # Degree
    beta = (180.0 - 360.0/number_of_sides) # Degree
    side_l = (2*(radius_of_circle**2) - 2*(radius_of_circle**2)*np.cos(alpha * np.pi / 180))**0.5 # Radians
    
    for i in range(number_of_sides):
        turtle.left(180 - beta)
        turtle.forward(side_l)
    
    margin += 5
   

def draw_polygon():
    global r_const
    for i in range(3, 13, 1):
        regular_polygon(i, r_const)
        r_const += 5
        

draw_polygon()

turtle.down()
        
