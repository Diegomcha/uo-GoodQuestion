from opts import ITEMS, QUALITIES, SHIRTS_NAMES, PANTS_NAMES, SHOES_NAMES, PIJAMAS_NAMES, BASE_DAMAGE_WEAPON, ROOMS
from utils.functions import decide_list, decide_index_rated_list, ask_int
from game.game_manager import manager


def generate(available):
    item = {
        'type': decide_list(available) if type(available[0]) is str else available[decide_index_rated_list(available)]['type'],
        'quality': decide_index_rated_list(QUALITIES)
    }
    item['name'] = decide_list(ITEMS[item['type']]['names']) if not QUALITIES[item['quality']]['special'] else decide_list(ITEMS[item['type']]['special_names'])
    item['traits'] = ITEMS[item['type']]['traits'][item['quality']]
    item['consumable'] = ITEMS[item['type']]['consumable']
    item['damage'] = None if item['type'] != 'weapon' else BASE_DAMAGE_WEAPON[item['name']] + (4-int(QUALITIES[item['quality']]['id']))

    if item['type'] != 'clothes':
        item['part_of_body'] = None
    else:
        if item['name'] in SHIRTS_NAMES:
            item['part_of_body'] = 'shirt'
        elif item['name'] in PANTS_NAMES:
            item['part_of_body'] = 'pants'
        elif item['name'] in SHOES_NAMES:
            item['part_of_body'] = 'shoes'
        elif item['name'] in PIJAMAS_NAMES:  # pijama
            item['part_of_body'] = 'pijama'

    item['traits']['heal'] = None if item['type'] != 'medicine' else 1

    return item


def generate_key(number):
    item = {
        'type': 'key',
        'number': number
    }
    return item


def display(item):
    print(f"· {item['name']} [{QUALITIES[item['quality']]['name']}]")
    print(f"  {item['type']}{' - CONSUMABLE' if item['consumable'] else ''}")


#
# Private Method
def ask_if_continue(lose, win, room):
    if lose != None:
        print()
        if win['type'] == 'weapon':
            print(f"Are you willing to change the {lose['type']} [Name: {lose['name']} - Quality: {QUALITIES[lose['quality']]['name']} - Damage: {lose['damage']}]")
            print(f"For the {win['type']} [Name: {win['name']} - Quality: {QUALITIES[win['quality']]['name']} - Damage: {win['damage']}]")
        else:
            print(f"Are you willing to change the {lose['type']} [Name: {lose['name']} - Quality: {QUALITIES[lose['quality']]['name']} - Traits: {lose['traits']}]")
            print(f"For the {win['type']} [Name: {win['name']} - Quality: {QUALITIES[win['quality']]['name']} - Traits: {win['traits']}]")

        print()
        print(" 1 - [Yes] \n 2 - [No]")
        print()

        if ask_int(1, 2) == 1:
            room['chest'].append(lose)
            return True
        else:
            room['chest'].append(win)
            return False
    else:
        return True


##
# Public Method (In order to pick something USE this method)
def pick_items(item, quantity, character):
    room = ROOMS[character['room']['id']]

    if item['type'] == 'key':
        character['inventory']['keys'].append(item['number'])
        print(f"You have received a key")

    elif item['type'] == 'clothes':
        if item['part_of_body'] == 'shirt' and ask_if_continue(character['inventory']['clothes']['shirt'], item, room):
            character['inventory']['clothes']['shirt'] = item
            print(f"You have received a {item['name']}", end="")

        elif item['part_of_body'] == 'pants' and ask_if_continue(character['inventory']['clothes']['pants'], item, room):
            character['inventory']['clothes']['pants'] = item
            print(f"You have received a {item['name']}", end="")

        elif item['part_of_body'] == 'shoes' and ask_if_continue(character['inventory']['clothes']['shoes'], item, room):
            character['inventory']['clothes']['shoes'] = item
            print(f"You have received a {item['name']}", end="")

        elif item['part_of_body'] == 'pijama' and ask_if_continue(character['inventory']['clothes']['shirt'], item, room) and ask_if_continue(character['inventory']['clothes']['pants'], item, room):
            character['inventory']['clothes']['pijama'] = item
            print(f"You have received a {item['name']}", end="")

    elif item['type'] == 'medicine' or item['type'] == 'energetic_drink':
        for _ in range(quantity):
            character['inventory'][item['type']].append(item)
        print(f"You've received {quantity} {item['name']}{'s' if quantity > 1 else ''}", end="")

    elif item['type'] == 'faith_item' and ask_if_continue(character['inventory']['faith_item'], item, room):
        character['inventory']['faith_item'] = item
        print(f"You have received a {item['name']}", end="")

    elif item['type'] == 'weapon' and ask_if_continue(character['inventory']['weapon'], item, room):
        if character['inventory']['weapon'] == None:
            print(f"Do you want to grab the {item['type']} [Name: {item['name']} - Quality: {QUALITIES[item['quality']]['name']} - Damage: {item['damage']}]?")
            print("""
                1 - [YES]
                2 - [NO]
                
                """)
            if ask_int(1, 2) == 1:
                character['inventory']['weapon'] = item
                character['strength'] = character['difficulty']['strength'] + item['damage']
                print(f"You have received a {item['name']}", end="")
            else:
                ROOMS[character['room']['id']]['chest'].append(item)
                print("You stay as before", end="")
        else:
            print(f"You have received a {item['name']}", end="")

    else:
        print("You stay as before", end="")

    input()


def consume_item(item, character):

    if item['type'] == 'medicine':

        afterwards_hp = character['hp'] + item['traits']['hp']
        print()
        print(f"Do you want to use the item {item['name']}? [{character['hp']}hp -> {afterwards_hp if afterwards_hp <= character['maxhp'] else character['maxhp']}hp]")
        print("\n\t1 - [YES]\n\t2 - [NO]\n")

        if ask_int(1, 2) == 1:
            print('Item used', end="")
            character['hp'] = afterwards_hp if afterwards_hp <= character['maxhp'] else character['maxhp']
            character['inventory']['medicine'].remove(item)
        else:
            print("Item not used", end="")

        input()

    elif item['type'] == 'energetic_drink':

        swiftness = character['swiftness'] + item['traits']['swiftness']
        print()
        print(f"Do you want to use the item {item['name']}? [{character['swiftness']}sp -> {swiftness if swiftness <= 100 else 100}sp]")
        print("\n\t1 - [YES]\n\t2 - [NO]\n")

        if ask_int(1, 2) == 1:
            print('Item used', end="")
            character['swiftness'] = swiftness if swiftness <= 100 else 100
            character['inventory']['enegergetic_drinks'].remove(item)
        else:
            print("Item not used", end="")
