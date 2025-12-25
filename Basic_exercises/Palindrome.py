word = input("Enter the word ")
j = len(word) - 1 # Create second iter index

for i in range(0, len(word)): # Create first iter index
    if i == j:
        print("Your word is a Palindrome!!! ")
        break
    elif word[i].isdigit() or word[j].isdigit():
        print("Invalid word, try without integers ")
        break
    elif word[i] == word[j]:
        j = j - 1
    else:
        print("Your word is not a Palindrome!!! ")
        break
    