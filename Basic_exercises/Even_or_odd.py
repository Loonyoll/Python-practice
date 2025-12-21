answer = 1

while answer == 1 and answer != 0:
    value = float(input("Enter the value: "))

    if value % 2 == 0:
        print("It's even number!!! ")
    elif value % 2 != 0:
        print("It's odd number!!! ")
    else:
        print("Error ")
    
    answer = int(input("Do you want to continue? 1 - Yes|| 0 - No "))
