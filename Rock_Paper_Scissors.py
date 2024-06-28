import random

options = ("rock", "paper", "scissors")
play = True

while play == True:

    user = input("Choose rock, paper, or scissors: ")
    option = random.choice(options)

    if user.lower() == "rock" and option == "paper":
        print("Computer chooses paper you lose!")
    elif user.lower() == "paper" and option == "scissors":
        print("Computer chooses scissors you lose!")
    elif user.lower() == "scissors" and option == "rock":
        print("Computer chooses rock you lose!")
    elif user.lower() == "rock" and option == "scissors":
       print("Computer chooses scissors you win!")
    elif user.lower() == "paper" and option == "rock":
       print("Computer chooses rock you win!")
    elif user.lower() == "scissors" and option == "paper":
       print("Computer chooses paper you win!")
    else:
        print("you both choose the same thing its a tie!")

    Continue = input("Do you want to play again? (yes, no): ")
    if Continue.lower() == "no":
        play = False