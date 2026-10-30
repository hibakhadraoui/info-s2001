# Create a deck of 52 cards, then:
# 1-shuffle it randomly
# 2-draw the first card
# 3-go through the deck until a card with the same value is found
# 4-remember how many cards it took to reach the first pair
# 5-repeat 1000 times and calculate the average number of cards

import random

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ["hearts", "diamonds", "clubs", "spades"]

# Create the deck of 52 cards
deck = []
for suit in suits:
    for value in values:
        deck.append((value, suit))


def cards_until_first_pair():
    random.shuffle(deck)
    first_value = deck[0][0]  # draw the first card
    index = 1
    while deck[index][0] != first_value:
        index = index + 1
    return index + 1  # number of cards looked at, first card included


total = 0
run = 0
while run < 1000:
    total = total + cards_until_first_pair()
    run = run + 1

print("Average number of cards:", total / 1000)