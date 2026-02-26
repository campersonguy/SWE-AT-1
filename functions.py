import os, keyboard
import variables as v

def clearscreen():  # Clears the terminal
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def move(row, col):  # move cursor
    return f"\033[{row};{col}H"

def newline(column):
    return f"\n\033[{column}G"

def clearline():
    print(f"\033[2K", end="")

def on_event(event):  # keycheck
    keypress(event.name, event.event_type)


def keypress(name, type):
    match name, type:
        case "a", "down":
            v.cursor -= 1
        case "d", "down":
            v.cursor += 1
    print(f"{move(v.lines - 2, v.col + 13 + (26 * v.cursor))}{v.codes.bold}^{v.codes.reset}", end="")


def printcard(line, col, card):  # print a card
    values = card.split("-")
    if len(values) == 2:
        print(f"{move(line + 1, col)}┌{"─" * 23}┐{(newline(col) + "│" + (" " * 23) + "│") * 11}{newline(col)}└{"─" * 23}┘")
        print(f"{move(line + 2, col + 2)}{v.ranks[ord(values[0]) - 65]}{move(line + 12, col + 22)}{v.ranks[ord(values[0]) - 65]}")

        symbollist = v.symbols[values[0]]
        for symbol in symbollist:
            loc = symbol.split("-")
            print(f"{move(int(loc[0]) + line, int(loc[1]) + col)}{v.suits[values[1]]}")

    else:
        print(f"{move(line + 1, col)}┌{"─" * 23}┐{(newline(col) + "│" + ("/" * 23) + "│") * 11}{newline(col)}└{"─" * 23}┘")