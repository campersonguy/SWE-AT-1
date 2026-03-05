import os, keyboard, time, math
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

def error(text):
    print(f"{move(7, 0)}{v.codes.bold}{text}{v.codes.reset}")
    time.sleep(1.5)
    clearline(7)

def printui():
    print(f"{move(0, 0)}Control the cursor with WASD.\nSelect cards to play with SPACE.\nPlay your hand with ENTER, or pass turn with P.\n\nPlay Type: {v.plays[v.playtype]}")


# The big stuff ----------------------------------------------------------------------------------------------------- #


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
            elif v.cards[f"p{v.type}hand"][v.card] != "":
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

    v.cursor[0] = clamp(v.cursor[0], -3, 3 - v.cursor[1])
    v.cursor[1] = clamp(v.cursor[1], 0, 1)

    print(f"{move(v.lines - 2 - (v.cursor[1] * 19), v.col + 13 + (12 * v.cursor[1]) + (26 * v.cursor[0]))}{v.codes.bold}^{v.codes.reset}")

    printui()


def printcard(line, col, card):  # print a card
    if card == "empty":
        print(f"{move(line + 1, col)}┌{"─" * 23}┐{(newline(col) + "│" + (" " * 23) + "│") * 11}{newline(col)}└{"─" * 23}┘")
        return

    values = card.split("-")
    try:
        count = v.selected.count(v.cards[f"p{v.turn}hand"].index(card))
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
        printcard(v.lines - 35, v.col - 65 + (26 * val), v.cards[f"p{v.turn}hand"][val])
    else:
        printcard(v.lines - 16, v.col - 78 + (26 * (val - 6)), v.cards[f"p{v.turn}hand"][val])


def play(list):
    card = []
    for i in range(len(v.selected)):
        card.append(v.cards[f"p{v.turn}hand"][list[i]].split("-"))

    if len(list) == 1 and v.playtype == 0 or len(list) == 2 and v.playtype == 1 or len(list) == 3 and v.playtype == 2 or 3 <= len(list) <= v.maxstraight and v.playtype == 4:
        if v.cards["pile"][len(v.cards["pile"]) - 1].split("-") < card[0]:
            v.cards["pile"].append(v.cards[f"p{v.turn}hand"][list[0]])
            for index in list:
                v.cards[f"p{v.turn}hand"][index] = ""
                printhand(index)
            v.selected.clear()

            if v.turn == 1:
                v.turn = 2
            else:
                v.turn = 1

            for i in range(13):
                printhand(i)

            if len(v.cards["pile"]) > 0:
                printcard(math.floor(v.lines / 2 - 30), v.col, v.cards["pile"][len(v.cards["pile"]) - 1])
            else:
                printcard(math.floor(v.lines / 2 - 30), v.col, "empty")

        else:
            error("Your card is not higher than the last played card!")
    else:
        error("You're playing the wrong type of hand!")


def skip():
    v.cards["pile"].clear()
    v.cards["pile"].append("")

    if v.turn == 1:
        v.turn = 2
    else:
        v.turn = 1

    for i in range(13):
        printhand(i)

    if len(v.cards["pile"]) > 0:
        printcard(math.floor(v.lines / 2 - 30), v.col, v.cards["pile"][len(v.cards["pile"]) - 1])
    else:
        printcard(math.floor(v.lines / 2 - 30), v.col, "empty")
