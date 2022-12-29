import os

from utils.functions import ask_int, print_file

TITLE_FILEPATH = os.path.join(os.path.curdir, "utils", "assets", "title.txt")
CREDITS_FILEPATH = os.path.join(os.path.curdir, "utils", "assets", "credits.txt")
LORE_FILEPATH = os.path.join(os.path.curdir, "utils", "assets", "lore.txt")

NEW_GAME = 1
ACHIEVEMENTS = 2
CREDITS = 3
EXIT = 4

# Main methods


def display():
    """
    Displays main menu.

    Returns
    -------
    int
        Actions selected (1. New game, 2. Achievements).
    """
    print()
    print_file(TITLE_FILEPATH)
    print()
    print('\t\t1 - [New game]')
    print('\t\t2 - [Achievements]')
    print('\t\t3 - [Credits]')
    print()
    print('\t\t4 - [Exit] 🥲')
    print()
    selection = ask_int(1, 4)

    if selection == CREDITS:
        print_file(CREDITS_FILEPATH)
        input()
        return display()
    if selection == EXIT:
        exit()

    return selection


def display_lore():
    """
    Displays the lore.
    """
    f = open(LORE_FILEPATH, 'r')
    for line in f:
        if line == '\n':
            input()
        else:
            print(line, end='')
    f.close()
