import os, keyboard
import variables as v


# Basic Commands ---------------------------------------------------------------------------------------------------- #


def clear():  # Clears the terminal
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def move(row, col):  # move cursor
    return f"\033[{row};{col}H"

def newline(column):
    return f"\n\033[{column}G"

def clearline(row):
    print(f"{move(row, 0)}\033[2K", end="")

def clamp(val, min_val, max_val):
    return max(min_val, min(val, max_val))

def on_event(event):  # keycheck
    keypress(event.name, event.event_type)


# the big stuff ----------------------------------------------------------------------------------------------------- #


def keypress(name, type):
    clearline(v.lines - 2)
    clearline(v.lines - 21)
    match name, type:
        case "w", "down":
            v.cursor[1] += 1
        case "s", "down":
            v.cursor[1] -= 1
        case "a", "down":
            v.cursor[0] -= 1
        case "d", "down":
            v.cursor[0] += 1

    if v.cursor[1] == 0:
        v.cursor[0] = clamp(v.cursor[0], -3, 3)
    if v.cursor[1] == 1:
        v.cursor[0] = clamp(v.cursor[0], -3, 2)

    v.cursor[1] = clamp(v.cursor[1], 0, 1)

    if v.cursor[1] == 0:
        print(f"{move(v.lines - 2, v.col + 13 + (26 * v.cursor[0]))}{v.codes.bold}^{v.codes.reset}")
    if v.cursor[1] == 1:
        print(f"{move(v.lines - 21, v.col + 25 + (26 * v.cursor[0]))}{v.codes.bold}^{v.codes.reset}")


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


def printhand():
    for i in range(13):
        if i < 6:
            printcard(v.lines - 35, v.col - 65 + (26 * i), v.cards["p1hand"][i])
        else:
            printcard(v.lines - 16, v.col - 78 + (26 * (i - 6)), v.cards["p1hand"][i])