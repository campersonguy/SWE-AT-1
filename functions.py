import os
from variables import *

def clearscreen():  # Clears the terminal
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def move(row, col):  # move cursor
    return f"\033[{row};{col}H"

def newline(column):
    return f"\n\033[{column}G"


def printcard(line, col, card):  # print a card
    values = card.split("-")
    print(f"{move(line + 1, col)}┌{"─" * 23}┐{(newline(col) + "│" + (" " * 23) + "│") * 11}{newline(col)}└{"─" * 23}┘")
    print(f"{move(line + 2, col + 2)}{ranks[ord(values[1]) - 65]}{move(line + 12, col + 22)}{ranks[ord(values[1]) - 65]}")

    symbollist = symbols[values[1]]
    for symbol in symbollist:
        loc = symbol.split("-")
        print(f"{move(int(loc[0]) + line, int(loc[1]) + col)}{suits[values[0]]}")