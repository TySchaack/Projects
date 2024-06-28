import random

play = True
options = ["Wild!",
           "Bar", "Bar",
           "Cherry", "Cherry",
           "Orange", "Orange",
           "Berry", "Berry"]

#the main game
while play == True:
    #initialize changing variables
    display = []

    #start the game
    input("Press enter to play!")

    #get each slot in the display
    i = 0
    while i < 3:
        display.append(random.choice(options))
        print(display)
        i += 1

    #make each slot comparable
    slot1 = display[0]
    slot2 = display[1]
    slot3 = display[2]

    #detect wilds
    if slot3 == "Wild!" and slot1 != "Wild!":
        slot3 = slot1
    elif slot3 == "Wild!" and slot2 != "Wild!":
        slot3 = slot2

    if slot2 == "Wild!" and slot3 != "Wild!":
        slot2 = slot3
    elif slot2 == "Wild!" and slot1 != "Wild!":
        slot2 = slot1

    if slot1 == "Wild!" and slot2 != "Wild!":
        slot1 = slot2
    elif slot1 == "Wild!" and slot3 != "Wild!":
        slot1 = slot3

    #find if the player is a winner
    if slot1 == slot2 and slot2 == slot3:
        winner = True
    else:
        winner = False

    #print if they won or not
    if winner == True:
        print("You Win!")
    else:
        print("You Lose!")

    #ask if they want to keep playing
    while True:
        Continue = input("Do you want to play again? (yes, no): ")
        if Continue.lower() == "no":
            play = False
            break
        elif Continue.lower() == "yes":
            play = True
            break
        else:
            print("That is not a valid option!")
print("Thanks for playing!")