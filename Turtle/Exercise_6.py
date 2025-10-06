# Exercise 6
import turtle

n = int(input("Enter number of paws: "))
alpha_0 = 360 // n
alpha = 0
turtle.shape('turtle')

for i in range(n):
    turtle.forward(150)
    turtle.stamp() # Leave a turtle stamp
    turtle.home()
    alpha += alpha_0 
    turtle.right(alpha)

