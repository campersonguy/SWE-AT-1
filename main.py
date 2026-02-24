import os, random, shutil, math, time
from variables import *
from functions import *

p1hand = []
p2hand = []

random.shuffle(cards["deck"])
for i in range(13):
    card = cards["deck"].pop(i)
    p1hand.append(card)
for i in range(13):
    card = cards["deck"].pop(i)
    p2hand.append(card)

p1hand.sort()

printcard(lines - 27, col - 65, p1hand[0])
printcard(lines - 27, col - 39, p1hand[1])
printcard(lines - 27, col - 13, p1hand[2])
printcard(lines - 27, col + 13, p1hand[3])
printcard(lines - 27, col + 39, p1hand[4])
printcard(lines - 27, col + 65, p1hand[5])
printcard(lines - 14, col - 78, p1hand[6])
printcard(lines - 14, col - 52, p1hand[7])
printcard(lines - 14, col - 26, p1hand[8])
printcard(lines - 14, col, p1hand[9])
printcard(lines - 14, col + 26, p1hand[10])
printcard(lines - 14, col + 52, p1hand[11])
printcard(lines - 14, col + 78, p1hand[12])


print(p1hand)

while True:
    i = 0




# card = input(f"{move(14, 0)}What card? ")
# values = card.split("-")
# if len(values) == 2:
#     printcard(lines, col, card)
# else:
#     clearscreen()
#     print("Not a real card\nUse format (first letter of suit)-(rank)")
#     time.sleep(2)
