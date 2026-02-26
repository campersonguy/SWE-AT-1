import os, random, shutil, math, time, keyboard
import variables as v
from functions import *

random.shuffle(v.cards["deck"])
for i in range(13):
    card = v.cards["deck"].pop(i)
    v.cards["p1hand"].append(card)
for i in range(13):
    card = v.cards["deck"].pop(i)
    v.cards["p2hand"].append(card)

v.cards["p1hand"].sort()

printcard(v.lines - 35, v.col - 65, v.cards["p1hand"][0])
printcard(v.lines - 35, v.col - 39, v.cards["p1hand"][1])
printcard(v.lines - 35, v.col - 13, v.cards["p1hand"][2])
printcard(v.lines - 35, v.col + 13, v.cards["p1hand"][3])
printcard(v.lines - 35, v.col + 39, v.cards["p1hand"][4])
printcard(v.lines - 35, v.col + 65, v.cards["p1hand"][5])
printcard(v.lines - 16, v.col - 78, v.cards["p1hand"][6])
printcard(v.lines - 16, v.col - 52, v.cards["p1hand"][7])
printcard(v.lines - 16, v.col - 26, v.cards["p1hand"][8])
printcard(v.lines - 16, v.col, v.cards["p1hand"][9])
printcard(v.lines - 16, v.col + 26, v.cards["p1hand"][10])
printcard(v.lines - 16, v.col + 52, v.cards["p1hand"][11])
printcard(v.lines - 16, v.col + 78, v.cards["p1hand"][12])

keyboard.hook(on_event)

while True:
    i = 0



# card = input(f"{move(14, 0)}What card? ")
# values = card.split("-")
# if len(values) == 2:
#     printcard(v.lines, v.col, card)
# else:
#     clearscreen()
#     print("Not a real card\nUse format (first letter of suit)-(rank)")
#     time.sleep(2)
