import random
import game.inventory_display as id
import game.character as char
from game.game_manager import manager
from utils.functions import ask_int


def monster_turn(character,monster):
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
        if random.randint(1,100) < monster['scape_rate']:
            print(f"The {monster['name']} ran away")
            input()
            return 'ran'
    if random.randint(0,2) == 0:
        print(f"The {monster['name']} growled!")
        input()
        return None

    else:
        print(f"{monster['name'].title()} decided to attack")
        input()
        ran_result = random.randint(0,101)
        if  ran_result > character['swiftness']:
            
            if ((ran_result-character['swiftness'])/100) < 0.3: 
                damage_dealt = monster['strength'] * (1-(ran_result-character['swiftness'])/100) - character['shield'] 
                print('The attack grazed your arm') 
                
            else:
                damage_dealt = monster['strength']-character['shield']
                print('You failed to dodge the attack')
                
            character['hp'] -= round(damage_dealt)
            
            input()
            print(f"You have received {round(damage_dealt)}hp of damage")
            input()
            
        else:
            print(f"You dodged the {monster['name']}'s attack!")
            input()
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
    print("Your turn to act!")
    while True:
        print("What will you do?")
        print('\t1 - [Attack]\t\t2 - [Use Object]')
        print()
        print('\t\t    3 - [Flee]')

        result = ask_int(1,3)

        if result == 1:
            #Monster try to evade
            if random.randint(0, 100) < monster['swiftness']:
                print(f"The {monster['name']} dodged the attack!")
                input()
                
            else:
                damage_dealt = character['strength']
                monster['hp'] -= damage_dealt
                print(f"You attacked! Dealt: {damage_dealt} damage.")
                input()
                
            break
        
        elif result == 2:
            invlen = len(character['inventory']['medicine']) + len(character['inventory']['energetic_drinks'])
            if invlen == 0:
                print("No consumable items")
                input()
            else:
                id.ask_use_items(character)
                
                if invlen != len(character['inventory']['medicine']) + len(character['inventory']['energetic_drinks']):
                    break

        elif result == 3:
            #Fleeing chance
            if random.randint(0,101) > character['swiftness']:
                print("You succesfully escaped!")
                return 'escaped'
            #If fails
            print(f"The {monster['name']} blocked your exit!")
            break
    
    return None


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
    print("||||||||||||||||||||||||||||||")
    print("||||||||COMBAT START!|||||||||")
    print("||||||||||||||||||||||||||||||")
    print("")

    turn = random.randint(0,1)
    while monster['hp'] > 0  and character['hp'] > 0:
        char.combat_display(character,monster)
        if turn == 0:
            if monster_turn(character, monster) == 'ran':
                return 0
            turn = 1
        elif turn == 1:
            if player_turn(monster, character) == 'escaped':
                manager['character_displayed'] = False
                print ("You were lucky back there huh?")
                input()
                return 'escaped'
            turn = 0
            
    if character['hp'] > 0:
        manager['character_displayed'] = False
        print(f"You succesfully killed the {monster['name']}")
        input()