import random, shutil, math

lines = shutil.get_terminal_size().lines
col = math.floor(shutil.get_terminal_size().columns / 2 - 12)


cards = {  # (suit-rank)
    "deck": ["S-0", "S-1", "S-2", "S-3", "S-4", "S-5", "S-6", "S-7", "S-8", "S-9", "S-10", "S-11", "S-12",
            "H-0", "H-1", "H-2", "H-3", "H-4", "H-5", "H-6", "H-7", "H-8", "H-9", "H-10", "H-11", "H-12",
            "C-0", "C-1", "C-2", "C-3", "C-4", "C-5", "C-6", "C-7", "C-8", "C-9", "C-10", "C-11", "C-12",
            "D-0", "D-1", "D-2", "D-3", "D-4", "D-5", "D-6", "D-7", "D-8", "D-9", "D-10", "D-11", "D-12",],
    "p1hand": [],
    "p2hand": [],
}

symbols = { # locations of symbols on the card
    "0": ["4-12", "7-12", "10-12"],
    "1": ["4-6", "4-18", "10-6", "10-18"],
    "2": ["4-6", "4-18", "7-12", "10-6", "10-18"],
    "3": ["3-6", "3-18", "7-6", "7-18", "11-6", "11-18"],
    "4": ["3-6", "3-18", "5-12", "7-6", "7-18", "11-6", "11-18"],
    "5": ["3-6", "3-18", "5-12", "7-6", "7-18", "9-12", "11-6", "11-18"],
    "6": ["3-6", "3-18", "5-6", "5-18", "7-12", "9-6", "9-18", "11-6", "11-18"],
    "7": ["3-6", "3-18", "4-12", "6-6", "6-18", "8-6", "8-18", "10-12", "11-6", "11-18"],
    "8": ["7-12"],
    "9": ["7-12"],
    "10": ["7-12"],
    "11": ["7-12"],
    "12": ["5-12", "9-12"],
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