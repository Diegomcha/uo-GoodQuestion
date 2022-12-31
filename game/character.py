import game.room as rm
import game.inventory as inv

from utils.functions import ask_options, ask_int, pause
from opts import KEYS, BASE_CHARACTERS, DIFFICULTIES, INVENTORY_SIZE, ROOMS


def display_difficulties():
    """
    Prints all the difficulties.
    """
    print("----- DIFFICULTY SELECTION -----")
    print()
    # prints number and difficulties
    for i, diff in enumerate(DIFFICULTIES):
        print(f"{i+1} - {diff['name']}")
    print()


def display_base_character(baseCharacter):
    """
    Prints the provided base character.

    Parameters
    ----------
    baseCharacter : dict[str, Any]
        The base character to print.
    """
    print('----- CHARACTER SELECTION -----')
    print()

    # name (blood)
    print(f"\t{baseCharacter['name']} ({baseCharacter['blood']})")
    # traits
    for trait_name, trait_value in baseCharacter['traits'].items():
        print(f"\t{'+' if trait_value >= 0 else '-'} {str(trait_value).lstrip('-')}% {trait_name}")
    print()


# Main methods
def select():
    """
    Module in charge of difficulty and character selection.

    Returns
    -------
    dict[str, Any]
        Returns the chosen character dict.
    """
    # Difficulty
    display_difficulties()
    difficulty = DIFFICULTIES[ask_int(1, len(DIFFICULTIES)) - 1]

    character = {
        'name': None,
        'maxhp': difficulty['maxhp'],
        'hp': 0,
        'shield': 0,
        'strength': difficulty['strength'],
        'sneak': difficulty['sneak'],
        'swiftness': difficulty['swiftness'],
        'last_room': 0,
        'visited_rooms': [],
        'remaining': difficulty['moves'],
        'inventory': [],
        'stats': {

        }
    }

    # Character
    id = 0
    selection = ''

    while selection != KEYS['select']:
        # Character stats
        display_base_character(BASE_CHARACTERS[id])

        # Asks for selection
        selection = ask_options({
            KEYS['select']: 'Select',
            KEYS['next']: 'Next',
            KEYS['previous']: 'Previous',
            KEYS['exit']: 'Exit'
        })

        # CHECK SELECTION
        # Select -> ends loop
        # Previous
        if selection == KEYS['next'] and id < (len(BASE_CHARACTERS) - 1):
            id += 1
        # Next
        elif selection == KEYS['previous'] and id > 0:
            id -= 1
        # Exit
        elif selection == KEYS['exit']:
            return

    # applies traits and name and initializes hp
    for trait, val in BASE_CHARACTERS[id]['traits'].items():
        character[trait] += (val / 100) * character[trait]
    character['name'] = BASE_CHARACTERS[id]['name']
    character['hp'] = character['maxhp']
    character['room'] = rm.generate(0, character['sneak'])

    return character


def display(character):
    """
    Prints the provided character.

    Parameters
    ----------
    character : dict[str, Any]
        Character to display.
    """
    print(f"----- {character['name']} ({character['remaining']} moves left) -----")
    print(f" - Health: {round(character['hp'], 1)} / {round(character['maxhp'], 1)}", end='')
    if character['shield'] != 0:
        print(f" ({round(character['shield'], 1)} shield)")
    else:
        print()
    print(f" - Strength: {round(character['strength'], 1)}")
    print(f" - Swiftness: {round(character['swiftness'], 1)}%")
    print(f" - Sneak: {round(character['sneak'], 1)}%")


def options(character):
    # TODO:
    if character['room']['monster'] != None:
        pass
    else:
        start = 1
        opts = ['move', 'inv']

        if character['room']['item'] != None:
            start += 1
            opts.insert(0, 'item')
            print(f"1 - Pick {character['room']['item']['name']}")

        print(f'{start} - Move to another room')
        print(f"{start + 1} - View inventory ({str(len(character['inventory'])) + ' / ' + str(INVENTORY_SIZE)})")
        print()
        # TODO: continue here

        return opts[ask_int(1, len(opts))-1]


def move(character):
    connections = character['room']['connections']

    for i, room_id in enumerate(connections):
        print(f"{i+1} - Open {i+1}º door and go inside [{'?????' if room_id not in character['visited_rooms'] else ROOMS[room_id]['resemblance']}]")
    print(f"{len(connections) +1} - Don't move")
    print()

    inp = ask_int(1, len(connections) + 1) - 1
    if inp == len(connections):
        return False

    lock = ROOMS[connections[inp]]['locked']
    if lock != None:
        key = inv.get_key(character['inventory'], lock)

        if key != None:
            inv.delete_item(character, key)
            ROOMS[connections[inp]]['locked'] = None
            print("The room is locked, you use your key to open it")
        else:
            print("The room is locked, you need a key")
            pause()
            return False

    character['room'] = rm.generate(connections[inp], character['sneak'])
    character['remaining'] -= 1
    return True


def pick_item(character):
    if len(character['inventory']) >= INVENTORY_SIZE:
        print(f"You must drop something before picking {character['room']['item']['name']}:")
        print()
        for id, item in enumerate(character['inventory']):
            print(f"{id + 1} - {item['name']}")
        print(f"{len(character['inventory']) + 1} - Do nothing")
        print()
        inp = ask_int(1, len(character['inventory']) + 1) - 1
        if inp == len(character['inventory']):
            return

        print(f"{character['inventory'][inp]['name']} was dropped")
        inv.delete_item(character, character['inventory'][inp])

    print(f"{character['room']['item']['name']} is now in your inventory")

    inv.add_item(character, character['room']['item'])
    character['room']['item'] = None

    pause()


def inventory(character):
    inv.display(character['inventory'])
    sel_item = inv.options(character['inventory'])
    if sel_item != None:
        print(f"Used {sel_item['name']}")
        inv.use_item(character, sel_item)
        inv.delete_item(character, sel_item)
        print()


def display_separator(character):
    print("-"*(len(character['name']) + len(str(character['remaining'])) + 26))
