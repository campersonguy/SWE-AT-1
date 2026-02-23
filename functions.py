import os
from variables import *

def clearscreen():  # Clears the terminal
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def move(row, col):  # move cursor
    return f"\033[{row};{col}H"

def newline():
    return f"\n\033[{col}G"


def printcard(line, col, values):  # print a card
    clearscreen()
    print(f"{move(line + 1, col)}┌{"─" * 23}┐{(newline() + "│" + (" " * 23) + "│") * 11}{newline()}└{"─" * 23}┘")
    print(f"{move(line + 2, col + 2)}{values[1]}{move(line + 12, col + 22)}{values[1]}")

    symbollist = symbols[values[1]]
    for symbol in symbollist:
        loc = symbol.split("-")
        print(f"{move(int(loc[0]) + line, int(loc[1]) + col)}{suits[values[0]]}")