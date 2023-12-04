"""
card n: winning numbers | your numbers
- first match = 1, all other matches is a double.
"""
import numpy as np
testing = False
if testing:
    scratchcards = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
                    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
                    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
                    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
                    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
                    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]
else:
    scratchcards = open('input.txt', 'r')
###################################################################


s = 0
for card in scratchcards:
    card = card.split(": ")[1].split(" | ")
    #
    m_numbers = []
    for m in card[1].split(" "):
        try:
            m_numbers.append(int(m))
        except ValueError:
            continue
    #
    w_numbers = []
    for w in card[0].split(" "):
        try:
            w_numbers.append(int(w))
        except ValueError:
            continue
    #
    score = 0
    for m in m_numbers:
        if m in w_numbers:
            if score == 0:
                score = 1
            else:
                score *= 2

    s += score
    print(s,":", score)

















###################################################################
if not testing:
    scratchcards.close()