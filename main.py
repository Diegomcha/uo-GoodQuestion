from game.main_menu import main_menu, NEW_GAME
from game.character_selector import character_selector
from game.achievement_display import start_painting


def main():
    """
    Main game loop
    """
    selection = main_menu()
    if selection == NEW_GAME:
        character = character_selector()
        if character == None:
            main()
        else:
            # TODO: Continue...
            print(character)
    else:
        start_painting()
        main()


main()
