import game.item as it
import game.main_menu as menu
import game.character as char
import game.achievement_display as achiev
import game.inventory_display as inv
import game.room as rm
import game.options as opt
import game.end as end
import game.combat_main as comb

from opts import ROOMS
from game.game_manager import manager


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
        print()
        print()
        print("------------- ADVENTURE STARTS! -------------")
        print()
        print()

        it.generate_attic_key()

        # Displays inital Room & character
        char.display(character)
        manager['displayed_character'] = True
        rm.display(character['room'], character)

        while character['remaining'] > 0 and character['hp'] > 0:
            char.set_elo(character)
            if character['room']['resemblance'] != 'attic':
                return_value = opt.display(ROOMS[character['room']['id']]['special_options'], character)
                if return_value == 'Another room':
                    monster = rm.move(character, character['room'])

                    if monster != None:
                        manager['enemies_found'] += 1
                        if comb.fight(character, monster) == 'escaped':
                            # make monster stay in the room
                            ROOMS[character['room']['id']]['monsters'] = {
                                'rate': 100+character['sneak'],
                                'available': [
                                    {
                                        'type': monster['type'],
                                        'rate': 100
                                    }
                                ]
                            }
                            character['room'] = character['last_room']

                elif return_value == 'Inventory':
                    inv.display_inventory(character)
                    manager['character_displayed'] = False
            else:
                break

        end.ending(character)


main()
