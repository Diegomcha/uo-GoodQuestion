import game.main_menu as menu
import game.character as char
import game.achievement_display as achiev
import game.room as rm


def main():
    """
    Main game loop
    """
    # Shows main menu
    selection = menu.display()

    # If achievements is selected
    if selection == menu.ACHIEVEMENTS:
        # Displays achievements menu and when the user leaves returns to the main menu
        achiev.display()
        return main()

    # If newgame is selected
    else:
        # Creates the character
        character = char.select()
        # If character creation is cancelled returns to main menu
        if character == None:
            return main()

        # Displays starting text (lore)
        menu.display_lore()

        # while character['remaining'] > 0:
        char.display(character)
        room = rm.generate(character['room'], character['sneak'])
        rm.display(room)

        # TODO: Continue...


main()
