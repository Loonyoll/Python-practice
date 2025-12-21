answer = 1

while answer == 1:
    t_value = 1
    value = int(input("Enter the value: "))
    
    if value < 0:
        print("Invalid value. It cannot be < 0. Please, try again. ")
    while value > 1:
        t_value = t_value * value
        value = value - 1
        
    print("It's = ", t_value)