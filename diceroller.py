# Imports
import random
import sys

#Setting up function

def rollDice():

    choice = input("Do you want to roll the dice? Type y/n: ") #Wait for input

    if choice == "y": #If yes
        number = random.randint(1, 6)

        print(f"Its >{number}<")
        rollDice()
    elif choice == "n": #If no
        sys.exit()
    else: #If the user types an invalid option (anything else except y and n)
        print("That is not a valid option!")
        rollDice()
        
rollDice() #Run the function