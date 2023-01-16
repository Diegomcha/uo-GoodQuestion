from opts import ITEMS, QUALITIES, SHIRTS_NAMES, PANTS_NAMES, SHOES_NAMES, PIJAMAS_NAMES, ROOMS
from utils.functions import decide_list, decide_index_rated_list, ask_int, pause
from game.game_manager import manager


def generate(available):
    """Method for generating the item having in mind the qualities and the type of item

    Parameters
    ----------
    available : list
        list containing the types of the items you want to generate
        (note that the program will pick one)

    Returns
    -------
    dict[str, Any]
        A dicitionary containing the attributes of the item
    """
    item = {
        'type': decide_list(available) if type(available[0]) is str else available[decide_index_rated_list(available)]['type'],
        'quality': decide_index_rated_list(QUALITIES)
    }
    item['name'] = decide_list(ITEMS[item['type']]['names']) if not QUALITIES[item['quality']]['special'] else decide_list(ITEMS[item['type']]['special_names'])
    item['traits'] = ITEMS[item['type']]['traits'][item['quality']]
    item['consumable'] = ITEMS[item['type']]['consumable']

    if item['type'] == 'clothes':
        if item['name'] in SHIRTS_NAMES:
            item['part_of_body'] = 'shirt'
        elif item['name'] in PANTS_NAMES:
            item['part_of_body'] = 'pants'
        elif item['name'] in SHOES_NAMES:
            item['part_of_body'] = 'shoes'
        elif item['name'] in PIJAMAS_NAMES:  # pijama
            item['part_of_body'] = 'pijama'

    return item


def generate_key(number):
    """Method that generates a key

    Parameters
    ----------
    number : int
        id of the key (id must match with the id of the door in order to open it)

    Returns
    -------
    dict[str, Any]
        dictionary containing the type ('key') and the number of it
    """
    item = {
        'type': 'key',
        'number': number
    }
    return item


def display(item):
    """Method that display the name of the item as well as some qualities

    Parameters
    ----------
    item : dict[str, Any]
        dictionary containing the attributes of the item
    """
    print(f"· {item['name']} [{QUALITIES[item['quality']]['name']}]")
    print(f"  {item['type']}{' - CONSUMABLE' if item['consumable'] else ''}")


#
# Private Method
def ask_if_continue(lose, win, room):
    """Method that asks if you want to change one item for another (shown qualities)

    Parameters
    ----------
    lose : dict[str, any]
        dictionary containing the item in your inventory
    win : dict[str, Any]
        dictionary containing the item you can get
    room : dict[str, Any]
        dictionary containing the attributes of the room

    Returns
    -------
    boolean
        True if the change is performed or if there is no change, else False
    """
    if lose != None:
        print()
        if win['type'] == 'weapon':
            print(f"Are you willing to change the {lose['type']} [Name: {lose['name']} - Quality: {QUALITIES[lose['quality']]['name']} - Damage: {lose['traits']['strength']}]")
            print(f"For the {win['type']} [Name: {win['name']} - Quality: {QUALITIES[win['quality']]['name']} - Damage: {win['traits']['strength']}]")
        else:  # TODO: bug with the traits
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
        if item['part_of_body'] == 'shirt' and ask_if_continue(character['inventory']['clothes']['shirt'], item, room) and ask_if_continue(character['inventory']['clothes']['pijama'], item, room):
            character['inventory']['clothes']['shirt'] = item
            character['sneak'] = character['difficulty']['sneak'] + item['traits']['sneak']
            print(f"You have received a {item['name']}")

        elif item['part_of_body'] == 'pants' and ask_if_continue(character['inventory']['clothes']['pants'], item, room) and ask_if_continue(character['inventory']['clothes']['pijama'], item, room):
            character['inventory']['clothes']['pants'] = item
            character['sneak'] = character['difficulty']['sneak'] + item['traits']['sneak']
            print(f"You have received a {item['name']}")

        elif item['part_of_body'] == 'shoes' and ask_if_continue(character['inventory']['clothes']['shoes'], item, room):
            character['inventory']['clothes']['shoes'] = item
            character['sneak'] = character['difficulty']['sneak'] + item['traits']['sneak']
            print(f"You have received a {item['name']}")

        elif item['part_of_body'] == 'pijama' and ask_if_continue(character['inventory']['clothes']['shirt'], item, room) and ask_if_continue(character['inventory']['clothes']['pants'], item, room):
            character['inventory']['clothes']['pijama'] = item
            character['sneak'] = character['difficulty']['sneak'] + item['traits']['sneak']
            print(f"You have received a {item['name']}")
        else:
            print("You stay as before")

    elif item['type'] == 'medicine' or item['type'] == 'energetic_drinks':
        for _ in range(quantity):
            character['inventory'][item['type']].append(item)
        print(f"You've received {quantity} {item['name']}{'s' if quantity > 1 else ''}")

    elif item['type'] == 'faith_item' and ask_if_continue(character['inventory']['faith_item'], item, room):
        character['inventory']['faith_item'] = item
        character['shield'] = item['traits']['shield']
        print(f"You have received a {item['name']}")

    elif item['type'] == 'weapon' and ask_if_continue(character['inventory']['weapon'], item, room):
        if character['inventory']['weapon'] == None:
            print(f"Do you want to grab the {item['type']} [Name: {item['name']} - Quality: {QUALITIES[item['quality']]['name']} - Damage: {item['traits']['strength']}]?")
            print("""
                1 - [YES]
                2 - [NO]
                
                """)
            if ask_int(1, 2) == 1:
                character['inventory']['weapon'] = item
                character['strength'] = character['difficulty']['strength'] + item['traits']['strength']
                manager['weapons_taken'] += 1
                print(f"You have received a {item['name']}")
            else:
                ROOMS[character['room']['id']]['chest'].append(item)
                print("You stay as before")
        else:
            character['inventory']['weapon'] = item
            character['strength'] = character['difficulty']['strength'] + item['traits']['strength']
            manager['weapons_taken'] += 1
            print(f"You have received a {item['name']}")

    else:
        print("You stay as before")


def consume_item(item, character):
    """Method for consuming an item, adding its attribute to the character and removing it from the inventory

    Parameters
    ----------
    item : dict[str, Any]
        dictionary containing the attributes of the item to be consumed
    character : dict[str, Any]
        dictionary storing all the attributes of the character
    """
    if item['type'] == 'medicine':

        afterwards_hp = character['hp'] + item['traits']['hp']
        afterwards_hp = afterwards_hp if afterwards_hp <= character['maxhp'] else character['maxhp']

        print()
        print(f"Do you want to use the item {item['name']}? [{character['hp']}hp -> {afterwards_hp}hp]")
        print("\n\t1 - [YES]\n\t2 - [NO]\n")

        if ask_int(1, 2) == 1:
            print('Item used')
            manager['recovered_hp'] = afterwards_hp - character['hp']
            character['hp'] = afterwards_hp
            character['inventory']['medicine'].remove(item)
        else:
            print("Item not used")

    elif item['type'] == 'energetic_drinks':

        swiftness = character['swiftness'] + item['traits']['swiftness']
        swiftness = swiftness if swiftness <= 100 else 100

        print()
        print(f"Do you want to use the item {item['name']}? [{character['swiftness']}sp -> {swiftness}sp]")
        print("\n\t1 - [YES]\n\t2 - [NO]\n")

        if ask_int(1, 2) == 1:
            print('Item used')
            character['swiftness'] = swiftness
            character['inventory']['energetic_drinks'].remove(item)
        else:
            print("Item not used")

    pause()
