answer = 1

while answer == 1:
    
    operator = input("Enter operator +, -, *, /: ")
    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print("Invalid symbol, please try again ")
        continue
        
    f_value = float(input("Enter first value: "))
    s_value = float(input("Enter second value: "))
    
    if operator == '+':
        t_value = f_value + s_value 
        print(t_value)
    elif operator == '-':
        t_value = f_value - s_value
        print(t_value)
    elif operator == '*':
        t_value = f_value * s_value
        print(t_value)
    elif operator == '/':
        if s_value == 0:
            print("Error, s_value cannot be NULL, try again ")
        else:
            t_value = f_value / s_value
            print(t_value)
    else:
        print("Invalid symbol, please try again ")
        
    print("Do you want to continue? 1 - Yes||0 - No ")
    answer = input()
    