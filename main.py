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
                fight_won = False
                selected = char.options(character)

                if selected == 'move':
                    changed_room = char.move(character)
                elif selected == 'inv':
                    char.inventory(character)
                elif selected == 'item':
                    char.pick_item(character)
                elif selected == 'monster':
                    fight_won = char.fight(character)
                    if fight_won == 'flee':
                        changed_room = True
                    elif not fight_won:
                        break

                char.display(character)
                char.display_separator(character)

                if changed_room:
                    rm.display(character['room'], character)
                    char.display_separator(character)
                elif fight_won == True and character['room']['item'] != None:
                    rm.display_item(character['room'])
                    char.display_separator(character)


main()
