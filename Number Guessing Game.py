# Adding the necessary libraries
import random
import time

print("Hello my friend, welcome to the game")
time.sleep(1) 

# Adding step for say ending game
step = 1 

# Choosing difficulty
difficulty = input("Please choose the game difficulty \n Easy : 0,10 \n Normal : 0,100 \n Hard : 0,1000 \n")

# I'm making all the letters small because I don't want any mistakes
difficulty = difficulty.lower()

# If gamer choosing easy mode 
if difficulty == "easy":
    # Generate a number 
    number = random.randrange(-1,11)
    # Input a guessing
    guessing = int(input("Please say a number "))
    # If the prediction isn't correct, we want it to increase or decrease
    while number != guessing:
        step += 1
        if guessing < number :
            print("UP")
            guessing = int(input("Please say a number "))
        elif guessing > number :
            print("DOWN")
            guessing = int(input("Please say a number "))
        else:
            break
    print(f'Congratulations! You know in {step} steps')    

# If gamer choosing normal mode 
elif difficulty == "normal":
    # Generate a number
    number = random.randrange(-1,101)
    # Input a guessing
    guessing = int(input("Please say a number "))
    # If the prediction isn't correct, we want it to increase or decrease
    while number != guessing:
        step += 1
        if guessing < number :
            print("UP")
            guessing = int(input("Please say a number "))
        elif guessing > number :
            print("DOWN")
            guessing = int(input("Please say a number "))
        else:
            break
    print(f'Congratulations! You know in {step} steps')  

# If gamer choosing hard mode   
elif difficulty == "hard":
    # Generate a number
    number = random.randrange(-1,1001)
    # Input a guessing
    guessing = int(input("Please say a number "))
    # If the prediction isn't correct, we want it to increase or decrease
    while number != guessing:
        step += 1
        if guessing < number :
            print("UP")
            guessing = int(input("Please say a number "))
        elif guessing > number :
            print("DOWN")
            guessing = int(input("Please say a number "))
        else:
            break
    print(f'Congratulations! You know in {step} steps')   

# Finally, we thank you
print("Thank you for playing with me ")