import random
player_health = 10
player_strength = 10

monster_name = "rUPERTO"
monster_health = 10
monster_strength = 10
fleeing_chance = 1

def ask_int(start=0, end=0, msg='Selection: '):
    "ERRASE THIS FUNCTION FROM HERE"

    selection = ''
    while not (selection.lstrip('-').isdigit() and start <= int(selection) <= end):
        selection = input(msg).strip()
    print()

    return int(selection)

def monster_turn(player_health,monster_strength):
    option = random.randint(0,2)
    if option == 0:
        print("The " + str(monster_name) + " growled!")
        return(player_health)
    dodge_chance = random.randint(0,4+1)
    if dodge_chance == 0:
        print("You dodged the " + str(monster_name) + "´s attack!")
        return(player_health)
    player_health -= 5
    damage_dealt = monster_strength/2
    print("The " + str(monster_name) + " attacked, it dealt: " + str(damage_dealt))
    return(player_health)

def player_turn(monster_health, player_strength, fleeing_chance):
    print("What will you do?")
    print('\t\t1 - [Attack]')
    print()
    print('\t\t2 - [Flee]')

    selection = ask_int(1, 2)

    if selection == 1:
        evasion = random.randint(0,3)
        if evasion == 0:
            print("The " + str(monster_name) + " dodged the attack!")
            return(monster_health, fleeing_chance)
        monster_health-=5
        damage_dealt = player_strength/2
        print("You attacked! Dealt: " + str(damage_dealt) + " damage.")
        return(monster_health, fleeing_chance)

    elif selection == 2:
        fleeing_chance = random.randint(0,4)
        if fleeing_chance == 0:
            print("You succesfully escaped!")
            return(monster_health, fleeing_chance)
        print("The " + str(monster_name) + " blocked your exit!")
        return(monster_health, fleeing_chance)

print("||||||||||||||||||||||||||||||")
print("||||||||COMBAT! START!||||||||")
print("||||||||||||||||||||||||||||||")
print("")


while ((monster_health > 0) and (player_health > 0) and (fleeing_chance != 0)):
    turn_start = random.randint(0,2)
    if turn_start == 0:
        print(str(monster_name) + " rushed!")
        player_health = monster_turn(player_health,monster_strength)
        print("Player HP: " + str(player_health))
    elif turn_start == 1:
        print("Your turn to act!")
        monster_health, fleeing_chance = player_turn(monster_health,player_strength, fleeing_chance)
        print(str(monster_name)+ "´s HP: " + str(monster_health))

if fleeing_chance == 0:
    print ("You were lucky back there huh?")
elif monster_health <= 0:
    print ("You succesfully defeated the monster!")
else: 
    print("You died:(")






    







