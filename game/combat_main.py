import random
import game.inventory_display as id
import game.character as char
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
    if monster['hp'] < monster['maxhp']/2:
        if random.randint(1,100) < monster['scape_rate']:
            print(f"The {monster['name']} runed away")
            input()
            return 'runed'
    if random.randint(0,2) == 0:
        print(f"The {monster['name']} growled!")
        input()
        return(character['hp'])

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
        return(character['hp'])


def player_turn(monster, character):
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
            id.ask_use_items(character)
            if invlen != len(character['inventory']['medicine'])  + len(character['inventory']['energetic_drinks']):
                break

        elif result == 3:
            #Fleeing chance
            if random.randint(0,101) > character['swiftness']:
                print("You succesfully escaped!")
                return 'scaped'
            #If fails
            print(f"The {str(monster_name)} blocked your exit!")
            break
    
    return 0


def fight(character, monster):
    print("||||||||||||||||||||||||||||||")
    print("||||||||COMBAT! START!||||||||")
    print("||||||||||||||||||||||||||||||")
    print("")

    turn = random.randint(0,1)
    while monster['hp'] > 0  and character['hp'] > 0:
        char.combat_display(character,monster)
        if turn == 0:
            if monster_turn(character, monster) == 'runed':
                return 0
            turn = 1
        elif turn == 1:
            if player_turn(monster, character) == 'scaped':
                print ("You were lucky back there huh?")
                input()
                return 'scaped'
            turn = 0
            
    if character['hp'] > 0:
        print(f"You succesfully killed the {monster['name']}")
        input()