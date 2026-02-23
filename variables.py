import random, shutil, math

lines = math.floor(shutil.get_terminal_size().lines / 2 - 7)
col = math.floor(shutil.get_terminal_size().columns / 2 - 12)


cards = {  # (suit-rank)
    "deck": ["S-A", "S-2", "S-3", "S-4", "S-5", "S-6", "S-7", "S-8", "S-9", "S-10", "S-J", "S-Q", "S-K",
            "H-A", "H-2", "H-3", "H-4", "H-5", "H-6", "H-7", "H-8", "H-9", "H-10", "H-J", "H-Q", "H-K",
            "C-A", "C-2", "C-3", "C-4", "C-5", "C-6", "C-7", "C-8", "C-9", "C-10", "C-J", "C-Q", "C-K",
            "D-A", "D-2", "D-3", "D-4", "D-5", "D-6", "D-7", "D-8", "D-9", "D-10", "D-J", "D-Q", "D-K",],
    "p1hand": [],
    "p2hand": [],
}

symbols = { # locations of symbols on the card
    "A": ["7-12"],
    "2": ["5-12", "9-12"],
    "3": ["4-12", "7-12", "10-12"],
    "4": ["4-6", "4-18", "10-6", "10-18"],
    "5": ["4-6", "4-18", "7-12", "10-6", "10-18"],
    "6": ["3-6", "3-18", "7-6", "7-18", "11-6", "11-18"],
    "7": ["3-6", "3-18", "5-12", "7-6", "7-18", "11-6", "11-18"],
    "8": ["3-6", "3-18", "5-12", "7-6", "7-18", "9-12", "11-6", "11-18"],
    "9": ["3-6", "3-18", "5-6", "5-18", "7-12", "9-6", "9-18", "11-6", "11-18"],
    "10": ["2-6", "2-18", "4-12", "6-6", "6-18", "8-6", "8-18", "10-12", "12-6", "12-18"],
    "J": ["7-12"],
    "Q": ["7-12"],
    "K": ["7-12"],
}

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
    "S": "♠",
    "H": f"{codes.red}♥{codes.reset}",
    "C": "♣",
    "D": f"{codes.red}♦{codes.reset}",
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