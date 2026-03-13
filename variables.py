import random, shutil, math

lines = shutil.get_terminal_size().lines
col = math.floor(shutil.get_terminal_size().columns / 2 - 12)

cursor = [0, 0]
card = 0
selected = []

names = ["", ""]

cards = {  # (suit-rank)
    "deck": [
        "B-1", "C-1", "D-1", "E-1", "F-1", "G-1", "H-1", "I-1", "J-1", "K-1", "L-1", "M-1",
        "A-2", "B-2", "C-2", "D-2", "E-2", "F-2", "G-2", "H-2", "I-2", "J-2", "K-2", "L-2", "M-2",
        "A-3", "B-3", "C-3", "D-3", "E-3", "F-3", "G-3", "H-3", "I-3", "J-3", "K-3", "L-3", "M-3",
        "A-4", "B-4", "C-4", "D-4", "E-4", "F-4", "G-4", "H-4", "I-4", "J-4", "K-4", "L-4", "M-4",
    ],
    "p1hand": [],
    "p2hand": [],
    "p0hand": ["", "", "", "", "", "", "", "", "", "", "", "", ""],
    "pile": [""]
}

symbols = { # locations of symbols on the card
    "A": ["4-12", "7-12", "10-12"],
    "B": ["4-6", "4-18", "10-6", "10-18"],
    "C": ["4-6", "4-18", "7-12", "10-6", "10-18"],
    "D": ["3-6", "3-18", "7-6", "7-18", "11-6", "11-18"],
    "E": ["3-6", "3-18", "5-12", "7-6", "7-18", "11-6", "11-18"],
    "F": ["3-6", "3-18", "5-12", "7-6", "7-18", "9-12", "11-6", "11-18"],
    "G": ["3-6", "3-18", "5-6", "5-18", "7-12", "9-6", "9-18", "11-6", "11-18"],
    "H": ["3-6", "3-18", "4-12", "6-6", "6-18", "8-6", "8-18", "10-12", "11-6", "11-18"],
    "I": ["7-12"],
    "J": ["7-12"],
    "K": ["7-12"],
    "L": ["7-12"],
    "M": ["5-12", "9-12"],
}

playtype = 0

plays = ("Any", "High Card", "Pair", "Three of a Kind", "Four of a Kind", "Straight")

ranks = ("3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2")

# The maximum length of a straight, minimum is always 3, maximum is 13
maxstraight = 13

turn = 1

straightlen = 0
straightval = 0

detection = True

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
    darkblue = "\033[34m"

    orange = "\033[38;2;255;165;0m"

    italic = "\033[3m"
    reset = "\033[0m"

suits = {  # Suit characters
    "1": f"{codes.orange}♦{codes.reset}",
    "2": f"{codes.gray}♣{codes.reset}",
    "3": f"{codes.red}♥{codes.reset}",
    "4": f"{codes.reset}♠{codes.reset}",
}

titlecard = [
    "      _______ _     _      _                  ",
    "     |__   __| |   (_)    | |                 ",
    "        | |  | |__  _ _ __| |_ ___  ___ _ __  ",
    "        | |  | '_ \| | '__| __/ _ \/ _ \ '_ \ ",
    "        | |  | | | | | |  | ||  __/  __/ | | |",
    "        |_|  |_| |_|_|_|   \__\___|\___|_| |_|",
    "",
    "",
    "",
    "",
    "┏┓              ┓  ┓     ┏┓           ┳┳   ┏┓•  ┓•     ",
    "┗┓┏┓┏┓┏┓┏┏┓┏┓┏┓┏┫  ┣┓┓┏  ┣┫┏┳┓┓┏┏┓┏┓  ┃┃┏  ┣┫┓┏┓┃┓┏┓┏┓┏",
    "┗┛┣┛┗┛┛┗┛┗┛┛ ┗ ┗┻  ┗┛┗┫  ┛┗┛┗┗┗┻┛┗┗┫  ┗┛┛  ┛┗┗┛ ┗┗┛┗┗ ┛",
    "  ┛                   ┛            ┛                   ",
    "      Making your flights sussier by the second!"
    "",
    "",
    "",
    "",
    "             (Press SPACE to continue)",
]

tutorial = [
    "Welcome to Thirteen, the most card game ever of all time! I'll be teaching you how to play.",
    "",
    "At the start of the game, each player draws 13 cards from the deck.",
    "These cards will be organised by rank and suit, which will already be done for you.",
    "In this game, the highest card is a 2. So the card order is 3, 4, 5 [etc...], J, Q, K, 2.",
    "",
    "The player who goes first can start by playing any of the following hands: high card, pair, three of a kind, four of a kind or a straight.",
    "Straights can be any length, as long as it is more than 3, so you may see some devious straights from this game.",
    f"The player who goes next {codes.italic}has{codes.reset} to play the same type of hand you played. For example, if I play a pair, you have to play a pair.",
    "The hand you play next also has to be higher than the last player's hand. If it is the same, the suit has to be higher.\nThe suit order is diamonds lowest, clubs, hearts and spades highest.",
    "",
    "If you can't play a higher hand, or you just feel like it, you can pass your turn. The other player wins that round.",
    "The other player then gets to play any hand, just like at the start of the game.",
    "A player has won once they have played all the cards in their hand.",
    "",
    "When you play a straight, your opponent has to play a straight of the same length with a higher starting card.",
    "If I play a 4-5-6-7-8 straight, your straight must start on a card higher than 4.",
    "",
    "As soon as a player reaches zero cards, the game ends.",
    "Have fun!",
    "",
]

#  symbol locations - reference
#  |-----------------------|
#  |                       |
#  |     X           X     |
#  |     X     X     X     |
#  |           X           |
#  |     X           X     |
#  |     X     X     X     |
#  |     X           X     |
#  |           X           |
#  |     X     X     X     |
#  |     X           X     |
#  |                       |
#  |-----------------------|