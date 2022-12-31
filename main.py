import game.main_menu as menu
import game.character as char
import game.achievement_display as achiev
import game.room as rm

from opts import ROOMS


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
        main()

    # If newgame is selected
    else:
        # Creates the character
        character = char.select()
        # If character creation is cancelled returns to main menu
        if character == None:
            main()
        else:
            # Displays starting text (lore)
            menu.display_lore()

            # Displays inital Room & character
            char.display(character)
            char.display_separator(character)

            rm.display(character['room'], character)
            char.display_separator(character)

            while character['remaining'] > 0:  # TODO:
                changed_room = False
                selected = char.options(character)

                if selected == 'move':
                    changed_room = char.move(character)
                elif selected == 'inv':
                    char.inventory(character)
                elif selected == 'item':
                    char.pick_item(character)

                char.display(character)
                char.display_separator(character)

                if changed_room:
                    rm.display(character['room'], character)
                    char.display_separator(character)

            # char.display(character)
            # rm.display(character['room'], character)

            # while character['remaining'] > 0:
            #     opt.display(ROOMS[character['room']['id']]['special_options'], character)

            # TODO: Continue...


main()
