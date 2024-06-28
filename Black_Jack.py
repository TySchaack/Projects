import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
random.shuffle(cards)
play = True
player_busted = False

# The main brains behind the game
while play == True:

    game = True
    player_cards = []
    user_cards = []
    computer_cards = []
    comp_cards = []
    player_ace = False
    computer_ace = False

    # Gives the player and computer their starting cards
    random.shuffle(cards)
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))

    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

    # This is taking input from the player to decide if they want to hit, stand or if they busted
    while game == True:
        player_card_total = 0
        user_cards = []

        print(f"     Your cards:        {player_cards}")
        print(f"Computer's first card:   {computer_cards[0]}")

        Continue = input("Do you want to hit or stand? ")
        if Continue.lower() == "stand":
            game = False
        else:
            player_cards.append(random.choice(cards))

        i = 0
        while i < len(player_cards):
            card = player_cards[i]
            if card == 'J' or card == 'Q' or card == 'K':
                user_cards.append(10)
            elif card == "A":
                user_cards.append(11)
            else:
                user_cards.append(player_cards[i])
            i += 1

        for card in user_cards:
            player_card_total += card

        player_ace = "A" in player_cards

        if player_card_total > 21 and player_ace == False:
            player_busted = True
            break
        elif player_card_total > 21 and player_ace == True:
            user_cards.remove(11)
            user_cards.append(1)

            player_card_total = 0
            for card in user_cards:
                player_card_total += card

    if player_card_total > 21:
        player_busted = True

    # Try to make it so the computer will hit or stand
    cp_card_total = 0

    i = 0
    while i < len(computer_cards) and player_busted == False:
        card = computer_cards[i]
        if card == 'J' or card == 'Q' or card == 'K':
            comp_cards.append(10)
        elif card == "A":
            comp_cards.append(11)
        else:
            comp_cards.append(computer_cards[i])
        i += 1

    for card in comp_cards:
        cp_card_total += card

    while cp_card_total < 17 and player_busted == False:
        comp_cards = []
        cp_card_total = 0
        computer_cards.append(random.choice(cards))
        i = 0
        while i < len(computer_cards):
            card = computer_cards[i]
            if card == 'J' or card == 'Q' or card == 'K':
                comp_cards.append(10)
            elif card == "A":
                comp_cards.append(11)
            else:
                comp_cards.append(computer_cards[i])
            i += 1

        cp_card = 0
        j = 0
        while j < len(comp_cards):
            card1 = comp_cards[j]
            cp_card += card1
            j = j + 1
        cp_card_total = cp_card

    print(f"   Your cards:      {player_cards}")
    print(f" Computers cards:   {computer_cards}")
    if player_busted == True or player_card_total > 21:
        print("You busted, you lose")
    elif cp_card_total > 21:
        print("Computer busted you win")
    else:
        if cp_card_total > player_card_total:
            print("The computer wins! You lose!")
        elif cp_card_total < player_card_total:
            print("You win! The computer loses!")
        else:
            print("You tied! It's a push!")

    Continue = input("Do you want to play again? (yes, no): ")
    if Continue.lower() == "no":
        play = False
print("Thanks for playing")