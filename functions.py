import os, keyboard, time, math
import variables as v


# Commands ---------------------------------------------------------------------------------------------------- #


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

def error(text):
    print(f"{move(5, 0)}{v.codes.bold}{text}{v.codes.reset}")
    time.sleep(1.5)
    clearline(5)


# the big stuff ----------------------------------------------------------------------------------------------------- #


def keypress(name, type):  # Key Detection
    match name, type:
        case "w", "down":
            v.cursor[1] += 1
        case "s", "down":
            v.cursor[1] -= 1
        case "a", "down":
            v.cursor[0] -= 1
        case "d", "down":
            v.cursor[0] += 1
        case "space", "down":
            if v.card in v.selected:
                v.selected.remove(v.card)
            elif v.cards["p1hand"][v.card] != "":
                v.selected.append(v.card)
            printhand(v.card)
        case "enter", "down":
            play(v.selected)
            if len(v.cards["pile"]) > 0:
                printcard(math.floor(v.lines / 2 - 30), v.col, v.cards["pile"][len(v.cards["pile"]) - 1])
            else:
                printcard(math.floor(v.lines / 2 - 30), v.col, "empty")
        case "p", "down":
            skip()
    match type:
        case "down":
            clearline(v.lines - 2)
            clearline(v.lines - 21)

    if v.cursor[1] == 0:
        v.cursor[0] = clamp(v.cursor[0], -3, 3)
    if v.cursor[1] == 1:
        v.cursor[0] = clamp(v.cursor[0], -3, 2)

    v.cursor[1] = clamp(v.cursor[1], 0, 1)

    if v.cursor[1] == 0:
        print(f"{move(v.lines - 2, v.col + 13 + (26 * v.cursor[0]))}{v.codes.bold}^{v.codes.reset}")
    if v.cursor[1] == 1:
        print(f"{move(v.lines - 21, v.col + 25 + (26 * v.cursor[0]))}{v.codes.bold}^{v.codes.reset}")

    printui()


def printcard(line, col, card):  # print a card
    if card == "empty":
        print(f"{move(line + 1, col)}┌{"─" * 23}┐{(newline(col) + "│" + (" " * 23) + "│") * 11}{newline(col)}└{"─" * 23}┘")
        return

    values = card.split("-")
    try:
        count = v.selected.count(v.cards["p1hand"].index(card))
        if count > 0:
            print(f"{v.codes.yellow}", end="")
    except ValueError:
        count = 0

    if len(values) == 2:
        print(f"{move(line + 1, col)}┌{"─" * 23}┐{(newline(col) + "│" + (" " * 23) + "│") * 11}{newline(col)}└{"─" * 23}┘")
        print(f"{move(line + 2, col + 2)}{v.ranks[ord(values[0]) - 65]}{move(line + 12, col + 22)}{v.ranks[ord(values[0]) - 65]}")

        symbollist = v.symbols[values[0]]
        for symbol in symbollist:
            loc = symbol.split("-")
            print(f"{move(int(loc[0]) + line, int(loc[1]) + col)}{v.suits[values[1]]}")

    else:
        print(f"{v.codes.reset}{move(line + 1, col)}┌{"─" * 23}┐{(newline(col) + "│" + ("=" * 23) + "│") * 11}{newline(col)}└{"─" * 23}┘")
    
    print(f"{v.codes.reset}", end="")


def printhand(val):
    if val < 6:
        printcard(v.lines - 35, v.col - 65 + (26 * val), v.cards["p1hand"][val])
    else:
        printcard(v.lines - 16, v.col - 78 + (26 * (val - 6)), v.cards["p1hand"][val])

def printui():
    print(f"{move(0, 0)}Control the cursor with WASD.\nSelect cards to play with SPACE.\nPlay your hand with ENTER, or pass turn with P.")

def play(list):
    if len(list) == 1 and v.playtype == 0:
        card = v.cards["p1hand"][list[0]].split("-")[0]
        if v.cards["pile"][len(v.cards["pile"]) - 1].split("-")[0] < card:
            v.cards["pile"].append(v.cards["p1hand"][list[0]])
            for index in list:
                v.cards["p1hand"][index] = ""
                printhand(index)
            v.selected.clear()
        else:
            error("Your card is not higher than the last played card!")
    else:
        error("You're playing the wrong type of hand!")

def skip():
    v.cards["pile"].clear()
    v.cards["pile"].append("")