import random

play = True
coin_face = ["heads", "tails"]


while play == True:

    guess = input("Heads or Tails? ")
    win = random.choice(coin_face)

    if guess.lower() == win:
        print("You Win!")
    else:
        print("You Lose!")
    print(f"The coin landed on {win}!")

    Continue = input("Do you want to play again? (yes, no): ")
    if Continue.lower() == "no":
        play = False
print("Thanks for playing!")