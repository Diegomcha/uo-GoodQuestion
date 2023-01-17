import game.item as it
import game.character as char
import game.monsters as mon
from game.game_manager import manager

from opts import ROOMS, PREFABS
from utils.functions import decide, ask_int, pause


# Main methods
def display(room, character):
    """Method used to display the text when you enter a room

    Parameters
    ----------
    room : dict[str, Any]
        dictionary storing the values of the room to display
    character : dict[str, Any]
        dictionary storing the character attributes

    Returns
    -------
    dict[str, Any] / None
        The values of the monster found in the room
        None if the monster does not exist
    """

    if not room['id'] in character['visited_rooms']:
        print(f"You enter into a room that resembles a {room['resemblance']}")

        if room['resemblance'] != 'stairs':
            if room['id'] == manager['attic_key_room']:
                pause("...")
                it.pick_items(PREFABS['attic_key'], 1, character)
                pause()

            if room['monster'] == room['item'] == None:
                print("You find nothing inside")
            else:
                if room['item'] != None:
                    it.pick_items(room['item'], 1, character)

                if room['monster'] != None:
                    print(f"You find a monster!")
                    pause()
                    return room['monster']

    else:
        print(f"You return to the {room['resemblance']}")

    pause()


def search_keys(character, room):
    for key in character['inventory']['keys']:
        if room['locked'] == key['number']:
            return key
    return None


def unlock(character, room):
    """Method used for knowing if a room is unlocked

    Parameters
    ----------
    character : dict[str, Any]
        dictionary storing the attributes of the character
    room : dict[str, Any]
        dictionary storing the values of the room to display

    Returns
    -------
    boolean
        True if the room is unlocked or a key was used to unlock it
        else False
    """
    if room['locked'] == None:
        return True

    key = search_keys(character, room)
    if key != None:
        character['inventory']['keys'].remove(key)
        room['locked'] = None
        print('You unlock the door with the key you have in your inventory.')
        return True

    return False


def move(character, room):
    """Method for using to move

    Parameters
    ----------
    character : dict[str, Any]
        dictionary storing the attributes of the character
    room : dict[str, Any]
        dictionary storing the values of the room to display

    Returns
    -------
    dict[str, Any]
        A dict storing the attributes of the monster if there exists one
        else None
    """
    print(f"----- {room['resemblance'].upper()} -----")
    print()

    if room['resemblance'] != 'stairs':
        for i, id in enumerate(room['connections']):
            print(
                f"{i+1} - Door {i+1} [{'????' if (id not in character['visited_rooms']) else ROOMS[id]['resemblance']}]")
    else:
        print(
            f"1 - Top    [{'????' if (room['connections'][0] not in character['visited_rooms']) else ROOMS[room['connections'][0]]['resemblance']}]")
        print(
            f"2 - Mid    [{'????' if (room['connections'][1] not in character['visited_rooms']) else ROOMS[room['connections'][1]]['resemblance']}]")
        print(
            f"3 - Bottom [{'????' if (room['connections'][2] not in character['visited_rooms']) else ROOMS[room['connections'][2]]['resemblance']}]")

    print(f"{len(room['connections']) +1 } - Back")
    print()

    ask = ask_int(1, len(room['connections']) + 1)

    if (ask == len(room['connections']) + 1):
        manager['character_displayed'] = False
        return None
    else:
        where_to = room['connections'][ask - 1]

    if unlock(character, ROOMS[where_to]):
        character['last_room'] = character['room']
        character['visited_rooms'].append(character['room']['id'])
        character['room'] = generate(where_to, character['sneak'], character['difficulty']['name'], character['elo'])
        character['remaining'] -= 1
        char.display(character)
        manager['character_displayed'] = True
        monster = display(character['room'], character)
        if monster != None:
            return monster
    else:
        character['locked_doors_visited'].append(where_to)
        print("Seems to be locked")


# Main
def generate(id, sneak, difficulty, elo):
    """Method called whenever you want to generate a room in order to setup all the monsters/items

    Parameters
    ----------
    id : int
        id of the room
    sneak : int
        sneak of the character, the more sneak, the lesser monsters
    difficulty : string
        String of the name of the difficulty
    elo : int
        Power of the character

    Returns
    -------
    dict[str, Any]
        Dict storing the attributes of the room
    """
    room = ROOMS[id]

    item_rate = 0
    try:
        item_rate = room['items']['rate'] * 0.5 if difficulty == 'Hard' else room['items']['rate'] * \
            0.8 if difficulty == 'Medium' else room['items']['rate']
    except:
        pass

    monster_rate = 0
    try:
        monster_rate = room['monsters']['rate'] - sneak
    except:
        pass

    # generate item
    item = None
    # removes the possibility of an item appearing when the room has already been visited
    room['items']['rate'] = 0
    if decide(item_rate):  # if item is gonna be generated
        item = it.generate(room['items']['available'])

    # generate monster
    monster = None
    if decide(monster_rate):
        monster = mon.generate(room['monsters']['available'], difficulty, elo)

    return {
        'id': id,
        'resemblance': room['resemblance'],
        'connections': room['connections'],
        'item': item,
        'monster': monster
    }
