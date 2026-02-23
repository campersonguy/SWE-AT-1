import os, random, shutil, math, time
from variables import *
from functions import *

while True:
    card = input(f"{move(14, 0)}What card? ")
    values = card.split("-")
    if len(values) == 2:
        printcard(lines, col, values)
    else:
        clearscreen()
        print("Not a real card\nUse format (first letter of suit)-(rank)")
        time.sleep(2)