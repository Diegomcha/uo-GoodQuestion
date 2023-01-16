import random
import game.inventory_display as id
import game.character as char
import game.monsters as mon
from game.game_manager import manager
from utils.functions import ask_int, decide, pause


def monster_turn(character, monster):
    """Method including all the monster options depending on the difficulty
            - Deal damage
            - Growl
            - Escape

    Parameters
    ----------
    character : dict[str, Any]
        dictionary storing the character attributes
    monster : dict[str, Any]
        dictionary storing the monster attributes

    Returns
    -------
    string
        'ran' if the monster ran else None
    """
    # No attack
    if monster['hp'] < monster['maxhp']/2:
        if decide(monster['escape_rate']):
            print(f"The {monster['name']} ran away")
            pause()
            return 'ran'
    if decide(33):
        print(f"The {monster['name']} growled!")
        pause()
        return None

    else:
        print(f"{monster['name'].title()} decided to attack")
        ran_result = random.randint(0, 100)
        if ran_result > character['swiftness']:

            if ((ran_result-character['swiftness'])/100) < 0.3:
                damage_dealt = round(monster['strength'] * (1-(ran_result-character['swiftness'])/100) - character['shield'])
                print('The attack grazed your arm')

            else:
                damage_dealt = round(monster['strength']-character['shield'])
                print('You failed to dodge the attack')

            manager['damage_taken'] += 1
            character['hp'] -= damage_dealt

            print(f"You have received {damage_dealt} hp of damage")

        else:
            print(f"You dodged the {monster['name']}'s attack!")

        pause()
        return None


def player_turn(monster, character):
    """Method including the decisions of the player

    Parameters
    ----------
    character : dict[str, Any]
        dictionary storing the character attributes
    monster : dict[str, Any]
        dictionary storing the monster attributes

    Returns
    -------
    string
        'escaped' if player escaped, else None
    """
    print("What will you do?")
    print('\t1 - [Attack]\t\t2 - [Use Object]')
    print()
    print('\t\t    3 - [Flee]')

    result = ask_int(1, 3)

    if result == 1:
        # Monster tries to evade
        if decide(monster['swiftness']):
            print(f"The {monster['name']} dodged the attack!")

        else:
            damage_dealt = character['strength']
            manager['damage_dealt'] += damage_dealt
            monster['hp'] -= damage_dealt
            print(f"You attacked! Dealt: {damage_dealt} damage.")

        pause()

    elif result == 2:
        invlen = len(character['inventory']['medicine']) + len(character['inventory']['energetic_drinks'])
        if invlen == 0:
            print("No consumable items")
            pause()
        else:
            id.ask_use_items(character)

        # no item was used
        if invlen == len(character['inventory']['medicine']) + len(character['inventory']['energetic_drinks']):
            player_turn(monster, character)

    elif result == 3:
        # Fleeing chance
        if decide(character['swiftness']):
            return 'escaped'
        # If fails
        print(f"The {monster['name']} blocked your exit!")


def fight(character, monster):
    """Main loop for the combat

    Parameters
    ----------
    character : dict[str, Any]
        dictionary storing the character attributes
    monster : dict[str, Any]
        dictionary storing the monster attributes

    Returns
    -------
    string
        'escaped' if player escaped, else None
    """
    print("\t/|||||||||||||||||||||||||||||||||||||||\\")
    print("\t|||||||| C O M B A T  S T A R T |||||||||")
    print("\t\\|||||||||||||||||||||||||||||||||||||||/")
    print("")

    turn = random.randint(0, 1)
    while monster['hp'] > 0 and character['hp'] > 0:
        char.combat_display(character, monster)
        if turn == 0:
            if monster_turn(character, monster) == 'ran':
                return 0
            turn = 1
        elif turn == 1:
            print("Your turn to act!")
            if player_turn(monster, character) == 'escaped':
                manager['character_displayed'] = False
                print("You succesfully escaped!")
                print("You were lucky back there huh?")
                pause()
                return 'escaped'
            turn = 0

    if character['hp'] > 0:
        manager['character_displayed'] = False
        manager['enemies_defeated'] += 1
        print(f"You succesfully killed the {monster['name']}")

        gen_ghost = False

        if character['difficulty']['name'] == 'Hard' and decide(50):
            gen_ghost = True
        elif decide(33):
            gen_ghost = True

        if gen_ghost:
            print("The ghost of the monster has appeared to fight you!")
            pause()
            return fight(character, mon.generate_ghost(monster, character['difficulty'], character['elo']))

        pause()
