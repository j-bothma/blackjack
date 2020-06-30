import random


def create_deck():
    num_cards = [[str(i)] * 8 for i in range(1, 11)]
    face_cards = ["j", "q", "k", "a"]
    all_face_cards = [[i] * 8 for i in face_cards]
    all_cards = all_face_cards + num_cards
    final_cards = []

    for i in all_cards:
        final_cards += i

    random.shuffle(final_cards)
    return final_cards


def score():
    player_starts = 200
    return player_starts


def drawcard():
    deck = create_deck()
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0
    if len(player_cards) == 0:
        player_cards.append(deck.pop(0))
        player_cards.append(deck.pop(0))
        dealer_cards.append(deck.pop(0))
        dealer_cards.append(deck.pop(0))
    print("Your cards are : " + " ".join(player_cards))
    print("The dealer's cards are : " + " ".join(dealer_cards))

    for i in player_cards:
        if i.isnumeric():
            player_score += int(i)
        elif i == "a":
            if player_score + 10 <= 21:
                player_score += 10
            else:
                player_score += 1
        else:
            player_score += 10

    for i in dealer_cards:
        if i.isnumeric():
            dealer_score += int(i)
        elif i == "a":
            if dealer_score + 10 <= 21:
                dealer_score += 10
            else:
                dealer_score += 1
        else:
            dealer_score += 10

    print(player_score, dealer_score)

    while player_score < 21:
        choice = input("Do you want to 'hit' or 'stay'?")
        if choice == "hit":
            player_cards.append(deck.pop(0))
            for i in player_cards:
                if i.isnumeric():
                    player_score += int(i)
                elif i == "a":
                    if player_score + 10 <= 21:
                        player_score += 10
                    else:
                        player_score += 1
                else:
                    player_score += 10
            print(player_score, dealer_score)
        elif choice == "stay":
            break
        else:
            print("Please enter a valid response")

    if player_score > dealer_score:
        print("You win")
    elif player_score > dealer_score:
        print("You lose")
    else:
        print("You split the pot")

drawcard()
