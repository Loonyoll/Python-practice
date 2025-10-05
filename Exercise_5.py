# Exercise 5
import turtle 

const_margin_x = 0
const_margin_y = 0
turtle.shape('turtle')
for i in range(10):
    
    turtle.forward(25 + 2* abs(const_margin_x)) # Double left and right margin
    turtle.left(90)
    turtle.forward(25 + 2* abs(const_margin_x))
    turtle.left(90)
    turtle.forward(25 + 2* abs(const_margin_x))
    turtle.left(90)
    turtle.forward(25 + 2* abs(const_margin_x))
    turtle.left(90)
    
    
    const_margin_x -= 15 # New home_x position
    const_margin_y -= 15 # New home_y position
    turtle.penup() 
    turtle.goto(const_margin_x, const_margin_y) # Change start position 
    turtle.pendown()

    