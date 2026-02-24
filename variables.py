import random, shutil, math

lines = shutil.get_terminal_size().lines
col = math.floor(shutil.get_terminal_size().columns / 2 - 12)


cards = {  # (suit-rank)
    "deck": [
        "1-A", "1-B", "1-C", "1-D", "1-E", "1-F", "1-G", "1-H", "1-I", "1-J", "1-K", "1-L", "1-M",
        "2-A", "2-B", "2-C", "2-D", "2-E", "2-F", "2-G", "2-H", "2-I", "2-J", "2-K", "2-L", "1-M",
        "3-A", "3-B", "3-C", "3-D", "3-E", "3-F", "3-G", "3-H", "3-I", "3-J", "3-K", "3-L", "1-M",
        "4-A", "4-B", "4-C", "4-D", "4-E", "4-F", "4-G", "4-H", "4-I", "4-J", "4-K", "4-L", "1-M",
    ],
    "p1hand": [],
    "p2hand": [],
}

symbols = { # locations of symbols on the card
    "A": ["4-12", "7-12", "10-12"],
    "B": ["4-6", "4-18", "7-12", "10-6", "10-18"],
    "C": ["3-6", "3-18", "7-6", "7-18", "11-6", "11-18"],
    "D": ["3-6", "3-18", "5-12", "7-6", "7-18", "11-6", "11-18"],
    "E": ["3-6", "3-18", "5-12", "7-6", "7-18", "9-12", "11-6", "11-18"],
    "F": ["3-6", "3-18", "5-6", "5-18", "7-12", "9-6", "9-18", "11-6", "11-18"],
    "G": ["3-6", "3-18", "4-12", "6-6", "6-18", "8-6", "8-18", "10-12", "11-6", "11-18"],
    "H": ["7-12"],
    "I": ["7-12"],
    "J": ["7-12"],
    "K": ["7-12"],
    "L": ["5-12", "9-12"],
}

ranks = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]

# The suit order (default: Spades, Hearts, Clubs, Diamonds)
suitorder = ["S", "H", "C", "D"]

# The maximum length of a straight, minimum is always 3, maximum is 13
maxstraight = 13

# If four of a kind/three pair auto wins a round
stronghand = True


class codes:  # List of ANSI escape codes for coloured text and other stuff
    home =  "\033[H"
    clear = "\033[2K"
    bold = "\033[1m"
    pink = "\033[35m"
    gray = "\033[90m"
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    purple = "\033[95m"
    blue = "\033[96m"

    orange = "\033[38;2;255;165;0m"

    reset = "\033[0m"

suits = {  # Suit emojis
    "1": "♠",
    "2": f"{codes.red}♥{codes.reset}",
    "3": "♣",
    "4": f"{codes.red}♦{codes.reset}",
}


#  symbol locations - reference
#  |-----------------------|
#  |     X           X     |
#  |     X           X     |
#  |     X     X     X     |
#  |           X           |
#  |     X           X     |
#  |     X     X     X     |
#  |     X           X     |
#  |           X           |
#  |     X     X     X     |
#  |     X           X     |
#  |     X           X     |
#  |-----------------------|