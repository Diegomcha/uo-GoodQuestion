import random
import game.inventory_display as id
from utils.functions import ask_int

#All subtituted
player_health = 10
player_strength = 10

monster_name = "rUPERTO"
monster_health = 10
monster_strength = 10
fleeing_chance = 0


def monster_turn(character,monster):
    # No attack
    if random.randint(0,2) == 0:
        print(f"The {monster['name']} growled!")
        return(character['hp'])

    else:
        print(f"{monster['name'].title()} decided to attack")
        ran_result = random.randint(0,101)
        if  ran_result > character['swiftness']:
            damage_dealt = monster['strength'] * (1-(ran_result-character['swiftness'])/100) if ((ran_result-character['swiftness'])/100) < 0.3 else monster['strength']
            character['hp'] -= damage_dealt
            
            print('You failed to dodge the attack')
            print(f"You have received {damage_dealt}hp of damage")
            
        else:
            print(f"You dodged the {monster['name']}'s attack!")
            
        return(character['hp'])


def player_turn(monster, character):
    print("Your turn to act!")
    print("What will you do?")
    print('\t1 - [Attack]\t\t2 - [Use Object]')
    print('\t\t\t3 - [Flee]')

    result = ask_int(1,3)

    if result == 1:
        #Monster try to evade
        if random.randint(0, 101) > monster['swiftness']:
            print(f"The {monster['name']} dodged the attack!")

        else:
            damage_dealt = character['strenght']
            print(f"You attacked! Dealt: {damage_dealt} damage.")
    
    elif result == 2:
        id.ask_use_items(character)

    elif result == 3:
        #Fleeing chance
        if random.randint(0,101) > character['swiftness']:
            print("You succesfully escaped!")
            return 'scaped'
        #If fails
        print(f"The {str(monster_name)} blocked your exit!")
    
    return 0


def fight(character, monster):
    print("||||||||||||||||||||||||||||||")
    print("||||||||COMBAT! START!||||||||")
    print("||||||||||||||||||||||||||||||")
    print("")

    turn = random.randint(0,2)
    while monster['health'] >0  and character['hp'] > 0:
        if turn == 0:
            monster_turn(character, monster)
            turn = 1
        elif turn == 1:
            if player_turn(monster, character) == 'scaped':
                print ("You were lucky back there huh?")
                return 0
            turn = 0

