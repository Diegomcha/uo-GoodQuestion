
import random
from utils.functions import ask_int

#All subtituted
player_health = 10
player_strength = 10

monster_name = "rUPERTO"
monster_health = 10
monster_strength = 10
fleeing_chance = 1

def monster_turn(player_health,monster_strength):
    # No attack
    if random.randint(0,2) == 0:
        print(f"The {monster_name} growled!")
        return(player_health)

    elif random.randint(0,4+1) == 0:
        print(f"You dodged the {monster_name}'s attack!")
        return(player_health)
    
    #else:
    player_health -= 5
    damage_dealt = monster_strength/2
    print(f"The {monster_name} attacked, it dealt: {str(damage_dealt)}")
    return(player_health)

def player_turn(monster_health, player_strength, fleeing_chance):
    print("What will you do?")
    print('\t\t1 - [Attack]')
    print()
    print('\t\t2 - [Flee]')


    if ask_int(1, 2) == 1:
        #Monster try to evade
        if random.randint(0,3) == 0:
            print(f"The {monster_name} dodged the attack!")
            return(monster_health, fleeing_chance)
        #Evasion failed
        monster_health-=5
        damage_dealt = player_strength/2
        print(f"You attacked! Dealt: {str(damage_dealt)} damage.")
        return(monster_health, fleeing_chance)

    else:
        #Fleeing chance
        if random.randint(0,4) == 0:
            print("You succesfully escaped!")
            return(monster_health, fleeing_chance)
        #If fails
        print(f"The {str(monster_name)} blocked your exit!")
        return(monster_health, fleeing_chance)


def fight():
    print("||||||||||||||||||||||||||||||")
    print("||||||||COMBAT! START!||||||||")
    print("||||||||||||||||||||||||||||||")
    print("")

    turn = random.randint(0,2)
    while ((monster_health > 0) and (player_health > 0) and (fleeing_chance != 0)):
        if turn == 0:
            print(f"{monster_name} rushed!")
            player_health = monster_turn(player_health,monster_strength)
            print("Player HP: " + str(player_health))
            turn = 1
        elif turn == 1:
            print("Your turn to act!")
            monster_health, fleeing_chance = player_turn(monster_health,player_strength, fleeing_chance)
            print(f"{monster_name}'s HP: " + str(monster_health))
            turn = 0

    #These could be return messages since now is a method
    if fleeing_chance == 0:
        print ("You were lucky back there huh?")
    elif monster_health <= 0:
        print ("You succesfully defeated the monster!")
    else: 
        print("You died:(")






    







