with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

from collections import Counter

card_rankings = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def handToNum(hand):
    # Sample input: "32T3K". Output: [1, 0, 9, 1, 12]
    hand = [card_rankings.index(card) for card in hand]
    num = 0
    for i in hand:
        num = num * 13 + i
    return num

def handToPokerValue(hand):
    # Length of hand is 5.
    # 0, 1, 2, 3, 4, 5, 6
    # High card, One pair, Two pair, Three of a kind, Full House, Four of a kind, Five of a kind
    hand = Counter(hand)
    if len(hand) == 5:
        # High card
        return 0
    elif len(hand) == 4:
        # One pair
        return 1
    elif len(hand) == 3:
        # Two pair or Three of a kind
        if 3 in hand.values():
            # Three of a kind
            return 3
        else:
            # Two pair
            return 2
    elif len(hand) == 2:
        # Full House or Four of a kind
        if 2 in hand.values():
            # Full House
            return 4
        else:
            # Four of a kind
            return 5
    else:
        # Five of a kind
        return 6


hands = []
for line in lines:
    hand, value = line.split()
    hands.append((handToPokerValue(hand), handToNum(hand), int(value), hand))
hands.sort()
winnings = 0
for i, hand in enumerate(hands):
    winnings += hand[2] * (i + 1)
print(winnings)

