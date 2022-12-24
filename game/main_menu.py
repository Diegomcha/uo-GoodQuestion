from utils.functions import ask_int

TITLE_FILEPATH = "utils/assets/title.txt"
CREDITS_FILEPATH = "utils/assets/credits.txt"

NEW_GAME = 1
ACHIEVEMENTS = 2
CREDITS = 3
EXIT = 4


def print_file(file):
    """
    Prints the contents of the file.

    Parameters
    ----------
    file : str
        Path to the file whose contents to print.
    """

    f = open(file, 'r')
    for line in f:
        print(line)
    f.close()


def main_menu():
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
    print()

    if selection == CREDITS:
        print_file(CREDITS_FILEPATH)
        input()
        return main_menu()
    if selection == EXIT:
        exit()

    return selection
