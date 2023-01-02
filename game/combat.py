import game.room as rm
import game.character as char
import game.monster as mon

from utils.functions import decide


def display_attack(attack, attacker_type, defender):
    if attack == None:
        print("The monster dodges your attack" if attacker_type == 'character' else "You dodge the monster's attack")
    else:
        print(f"You deal {attack} damage to the monster ({defender['hp']} left)" if attacker_type == 'character' else f"You are damaged {attack} by the monster ({defender['hp']} left)")


def check_end(character, monster):
    if character['hp'] > 0 and monster['hp'] > 0:
        return False
    elif monster['hp'] <= 0:
        return 'character'
    else:
        return 'monster'


def attack(attacker, defender):
    if decide(100 - defender['swiftness']):  # if defender doesn't dodge
        hit = attacker['strength'] - defender['shield']
        if hit <= 0:  # if shield covers all damage
            return None

        defender['hp'] -= hit
        if defender['hp'] < 0:
            defender['hp'] = 0
        return attacker['strength']


def flee(character, monster):
    if decide(monster['flee']):
        aux = character['room']['id']
        character['room'] = rm.generate(character['last_room'], character)
        character['last_room'] = aux
        return True

    return False


def display_stats(character, monster):
    print("----- COMBAT -----")
    char.display_combat(character)
    print("------- VS -------")
    mon.display_combat(monster)
    print("-"*18)
