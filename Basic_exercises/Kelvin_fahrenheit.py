answer = 1

while answer == 1:
    k_choice = 1
    f_choice = 0
    choice = int(input("Enter your choice: from Fahrenheit to Kelvin - 1 or vice versa - 0: "))
    
    if choice == k_choice:
        f_value = float(input("Enter the Fahrenheit value: "))
        k_value = (5/9)*(f_value - 32) + 273
        print("It's = ", k_value)
    elif choice == f_choice:
        k_value = float(input("Enter the Kelvin value: "))
        f_value = (9/5)*(k_value - 273) + 32
        print("It's = ", f_value)
    else:
        print("Error ")
    
    answer = int(input("Do you want to contintue? 1 - Yes|| 0 - No: "))
    