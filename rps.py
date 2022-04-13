import random
import sys

av_bot_choices = ["rock", "paper", "scissors"]

def rps():
    choice = input("Lets play rock, paper, scissors! Whats your choice? rock/paper/scissors >>> ")

    bot_choice = random.choice(av_bot_choices)

    if choice == "rock":
        if bot_choice == "rock":
            print("I choose rock. Draw!\n"
                  "--------------------")
            rps()
        elif bot_choice == "paper":
            print("I choose paper. I win!\n"
                  "--------------------")
            rps()
        elif bot_choice == "scissors" or "scissor": # For toleration of a typo
            print("I choose scissors. You win!\n"
                  "--------------------")
            rps()
    elif choice == "paper":
        if bot_choice == "rock":
            print("I choose rock. You win!\n"
                  "--------------------")
            rps()
        elif bot_choice == "paper":
            print("I choose paper. Draw!\n"
                  "--------------------")
            rps()
        elif bot_choice == "scissors" or "scissor":
            print("I choose scissors. I win!\n"
                  "--------------------")
            rps()
    elif choice == "scissors":
        if bot_choice == "rock":
            print("I choose rock. I win!\n"
                  "--------------------")
            rps()
        elif bot_choice == "paper":
            print("I choose paper. You win!\n"
                  "--------------------")
            rps()
        elif bot_choice == "scissors" or "scissor":
            print("I choose scissors. Draw!\n"
                  "--------------------")
            rps()
    else:
        print(f"'{choice}' is not one of the options. Please try again")
        rps()

rps()
