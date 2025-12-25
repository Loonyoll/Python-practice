import random

answer = 1

while answer == 1:
    programm_choice = random.randint(1, 100)
    user_choice = int(input("Take a guess and pick an positive integer from 1 to 100: "))
    if user_choice == programm_choice:
        print("Congratulations!!! You win ")
    else:
        print("Program number = ", programm_choice)
        answer = int(input("You didn't guess. Do you want to continue? 1 - Yes||0 - No "))
    