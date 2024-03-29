import game.room as rm
import game.item as it

from utils.functions import ask_options, ask_int
from opts import KEYS, BASE_CHARACTERS, DIFFICULTIES


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
        'name': '',
        'maxhp': difficulty['maxhp'],
        'difficulty': difficulty,
        'hp': 'maxhp',
        'shield': 0,
        'strength': difficulty['strength'],
        'sneak': difficulty['sneak'],
        'swiftness': difficulty['swiftness'],
        'last_room': 0,
        'elo': 100,
        'visited_rooms': [],
        'remaining': difficulty['remaining'],
        'inventory': {'keys': [], 'medicine': [], 'energetic_drinks': [], 'clothes': {'shirt': None, 'pants': None, 'shoes': None, 'pijama': None}, 'faith_item': None, 'weapon': None},
        'traits': [],
        'locked_doors_visited': []
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
        character['difficulty'][trait] += (val / 100) * character['difficulty'][trait]
        character[trait] = character['difficulty'][trait]

    character['name'] = BASE_CHARACTERS[id]['name']
    character['hp'] = character['maxhp']
    character['room'] = rm.generate(0, character['sneak'], character['difficulty']['name'], character['elo'])
    character['last_room'] = character['room']['id']

    return character


def set_elo(character):
    character['elo'] = character['strength']*2 + character['shield']*3 + character['hp']


def display(character):
    """
    Prints the provided character.

    Parameters
    ----------
    character : dict[str, Any]
        Character to display.
    """
    title = f"----- {character['name']} ({character['remaining']} turn left) -----"

    print(f"\t{title}")
    print(f"\t - Health: {character['hp']} / {character['maxhp']}")
    print(f"\t - Strength: {character['strength']}")
    print(f"\t{'-' * len(title)}")
    print()


def combat_display(character, monster):
    monster_name = monster['name'].title() + " (" + monster['category']+")"
    print('*********************************************************')
    print(f"\t{character['name'].title()}\t\t|\t{monster_name}")
    print(f"\tHP: {character['hp']:.0f}\t\t|\tHP: {monster['hp']}")
    print(f"\tSHIELD: {character['shield']}\t|")
    print(f"\tSTRENGTH: {character['strength']}\t|\tSTRENGTH: {monster['strength']}")
    print('*********************************************************')
    print()
