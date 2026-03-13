import os, random, shutil, math, time, keyboard
import variables as v
from functions import *

print("\033[?25l")

time.sleep(0.5)
clear()

for i in range(len(v.titlecard)):
    print(f"{move(10 + i, v.col - 10)}{v.titlecard[i]}")
    time.sleep(0.05)

while not keyboard.is_pressed("space"):
    pass

for i in range(len(v.titlecard)):
    print(f"{move(10 + i, 0)}{" " * shutil.get_terminal_size().columns}")
    time.sleep(0.05)

clear()
time.sleep(0.5)


while True:
    print(f"{move(0, 0)}Your screen is {shutil.get_terminal_size().columns} columns wide and {shutil.get_terminal_size().lines} lines long.\nYour screen needs to be at least 208 columns wide and 61 lines long.\nPress SPACE to reload (or load you in if your screen is large enough).")
    while not keyboard.is_pressed("space"):
        pass
    if shutil.get_terminal_size().lines >= 1 and shutil.get_terminal_size().columns >= 1:
        clear()
        break
    clear()
    time.sleep(0.5)

v.lines = shutil.get_terminal_size().lines
v.col = math.floor(shutil.get_terminal_size().columns / 2 - 12)

print("\033[?25h", end="")
time.sleep(1)
v.names[0] = input("Player 1's name: ")
clear()
v.names[1] = input("Player 2's name: ")
clear()
time.sleep(1)

if input("Do you want to go through the tutorial? (Y/N) ").upper() != "N":
    clear()
    time.sleep(2)
    for line in v.tutorial:
        yap(line + "\n")
        time.sleep(2)

print(f"\033[?25l{clear()}", end="")

for i in range(3):
    print(f"Loading in {3 - i}...")
    time.sleep(1)
    clear()

random.shuffle(v.cards["deck"])
for i in range(2):
    for i1 in range(13):
        v.cards[f"p{i + 1}hand"].append(v.cards["deck"].pop())
    v.cards[f"p{i + 1}hand"].sort()

for i in range(13):
    printhand(i)

keyboard.hook(on_event)

printcard(9, v.col, v.cards["pile"][len(v.cards["pile"]) - 1])
printui()

while True:
    v.card = ((-v.cursor[1] + 1) * 6 + v.cursor[0] + 4) - 1