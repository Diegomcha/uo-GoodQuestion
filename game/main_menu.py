import os
import game.achievement_manager as am

from utils.functions import ask_int, print_file, pause
from opts import ACHIEVEMENTS_SAVE_PATH

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
    i = 2
    if am.check_file(ACHIEVEMENTS_SAVE_PATH):
        print('\t\t2 - [Achievements]')
        i += 1
    print(f'\t\t{i} - [Credits]')
    print()
    print(f'\t\t{i+1} - [Exit]')
    print()
    selection = ask_int(1, i+1)

    if selection == i:
        print_file(CREDITS_FILEPATH)
        pause()
        return display()
    if selection == i+1:
        exit()

    return selection


def display_lore():
    """
    Displays the lore.
    """
    print("\t\t\t\t----- LORE -----")
    f = open(LORE_FILEPATH, 'r', encoding='utf-8')
    for line in f:
        if line == '\n':
            pause()
        else:
            print(line, end='')
    f.close()
    print("\t\t\t\t----------------")
