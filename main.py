import os, random, shutil, math, time, keyboard
import variables as v
from functions import *

print("\033[?25l")

random.shuffle(v.cards["deck"])
for i in range(13):
    card = v.cards["deck"].pop(i)
    v.cards["p1hand"].append(card)
for i in range(13):
    card = v.cards["deck"].pop(i)
    v.cards["p2hand"].append(card)

v.cards["p1hand"].sort()

printhand()

keyboard.hook(on_event)

while True:
    v.card = ((-v.cursor[1] + 1) * 6 + v.cursor[0] + 4)
