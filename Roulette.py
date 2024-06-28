import random

play = True
player_money = 1000
nums = [0,00,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
colors = ["red","red","red","red","red","red","red","red","red",
          "black","black","black","black","black","black","black","black","black",
          "green"]

#the code behind the game
while play == True:
    #initialize all values that change
    can_bet = False
    can_guess = False
    color_num = ""

    #print how much money the player has to bet with
    print(f"You have ${player_money} to bet!")

    #get the players bet money amount
    bet = input("How much money would you like to bet? ")

    #make sure the player is betting only money they have
    while can_bet == False:
        if int(bet) <= player_money:
            can_bet = True
        else:
            print("You can not bet money you do not have!")
            bet = input("How much money would you like to bet? ")

    #find if the player is guessing the color or the number
    guess = input("Are you going to bet on the color or number? (color, number) ")

    #get the players guess of a number or color
    while can_guess == False:
        if guess.lower() == "color":
            final_guess = input("What color do you think it will land on? (red, black) ")
            color_num = "color"
            can_guess = True
        elif guess.lower() == "number":
            final_guess = input("What number do you think it will land on? (00, 0-36) ")
            color_num = "number"
            can_guess = True
        else:
            print("That is not something you can bet on! ")
            guess = input("Are you going to bet on the color or number? (color, number) ")

    #if a color guess choose the winning color
    if color_num == "color":
        win = random.choice(colors)
    #if a number guess choose the winning number
    elif color_num == "number":
        win = random.choice(nums)

    #compare the winning number or color to the players guess
    if str(win) == str(final_guess):
        winner = True
    else:
        winner = False

    #if color was right double the players bet
    if color_num == "color" and winner == True:
        player_money = player_money + int(bet)
        print(f"You win you guessed {final_guess} and the winning color was {win}!")
    elif color_num == "color" and winner == False:
        player_money = player_money - int(bet)
        print(f"You lose you guessed {final_guess} and the winning color was {win}!")

    #if number was right the player gets x36 their bet
    elif color_num == "number" and winner == True:
        player_money = player_money + int(bet) * 35
        print(f"You win you guessed {final_guess} and the winning number was {win}!")
    elif color_num == "number" and winner == False:
        player_money = player_money - int(bet)
        print(f"You lose you guessed {final_guess} and the winning number was {win}!")

    #get wether or not the player can continue playing and if they want to
    if player_money <= 0:
        print("You ran out of money! You are unlucky!")
        play = False
        break
    Continue = input("Do you want to play again? (yes, no): ")
    if Continue.lower() == "no":
        play = False
print("Thanks for playing!")
print(f"You are leaving with ${player_money}!")