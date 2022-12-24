from utils.functions import ask_options, ask_int
from opts import KEYS, CHARACTERS, DIFFICULTIES


def difficulties_print():
    """
    Prints all the difficulties.
    """
    print('----- DIFFICULTY SELECTION -----')
    print()

    # prints number and difficulties
    for i, diff in enumerate(DIFFICULTIES):
        print(f"{i+1} - {diff['name']}")

    print()


def character_print(character):
    """
    Prints the provided character.

    Parameters
    ----------
    character : dict[str, Any]
        The character to print.
    """
    print('----- CHARACTER SELECTION -----')
    print()

    # name (blood)
    print(f"\t{character['name']} ({character['blood']})")
    # traits
    for trait_name, trait_value in character['traits'].items():
        print(f"\t{'+' if trait_value >= 0 else '-'} {str(trait_value).lstrip('-')} {trait_name}")

    print()


# Public
def character_selector():
    """
    Module in charge of difficulty and character selection.

    Returns
    -------
    dict[str, Any]
        Returns the chosen character dict.
    """
    # Difficulty
    difficulties_print()
    difficulty = DIFFICULTIES[ask_int(1, len(DIFFICULTIES)) - 1]
    print()

    character = {
        'name': '',
        'maxhp': difficulty['maxhp'],
        'hp': 0,
        'strength': difficulty['strength'],
        'sneak': difficulty['sneak'],
        'swiftness': difficulty['swiftness'],
        'room': 0,
        'inventory': []
    }

    # Character
    id = 0
    selection = ''

    while selection != KEYS['select']:
        # Character stats
        character_print(CHARACTERS[id])

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
        if selection == KEYS['next'] and id < (len(CHARACTERS) - 1):
            id += 1
        # Next
        elif selection == KEYS['previous'] and id > 0:
            id -= 1
        # Exit
        elif selection == KEYS['exit']:
            return

        print()

    # applies traits and name and initializes hp
    for trait, val in CHARACTERS[id]['traits'].items():
        character[trait] += (val / 100) * character[trait]
    character['name'] = CHARACTERS[id]['name']
    character['hp'] = character['maxhp']

    return character
