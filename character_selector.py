from utils import ask_options, ask_int

# TODO: Documentation

# Characters
CHARACTERS = [
    {
        'name': 'Sam',
        'blood': 'AB+',
        'traits': {
            'swiftness': 1,
            'sneak': -1
        }
    },
    {
        'name': 'Sarah',
        'blood': '0-',
        'traits': {
            'strength': 1,
            'maxhp': -1
        }
    },
    {
        'name': 'Christa',
        'blood': '0+',
        'traits': {
            'sneak': 1,
            'swiftness': -1
        }
    },
    {
        'name': 'Mike',
        'blood': 'A+',
        'traits': {
            'maxhp': 1,
            'strength': -1
        }
    }
]

# Dificulties
DIFFICULTIES = [
    {
        'name': 'Easy',
        'maxhp': 0,
        'strength': 0,
        'sneak': 0,
        'swiftness': 0
    },
    {
        'name': 'Medium',
        'maxhp': 0,
        'strength': 0,
        'sneak': 0,
        'swiftness': 0
    },
    {
        'name': 'Hard',
        'maxhp': 0,
        'strength': 0,
        'sneak': 0,
        'swiftness': 0
    }
]


def difficulties_print():
    print('----- DIFFICULTY SELECTION -----')
    print()

    # prints number and difficulties
    for i, diff in enumerate(DIFFICULTIES):
        print(f"{i+1} - {diff['name']}")

    print()


def character_print(character):
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
    # Difficulty
    difficulties_print()
    difficulty = DIFFICULTIES[ask_int(1, len(DIFFICULTIES), 'Selection: ') - 1]
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

    while selection != 'S':
        # Character stats
        character_print(CHARACTERS[id])

        # Asks for selection
        selection = ask_options({
            'S': 'Select',
            'D': 'Next',
            'A': 'Previous',
            'E': 'Exit'
        })

        # CHECK SELECTION
        # Select -> ends loop
        # Previous
        if selection == 'D' and id < (len(CHARACTERS) - 1):
            id += 1
        # Next
        elif selection == 'A' and id > 0:
            id -= 1
        # Exit
        elif selection == 'E':
            exit()

        print()

    for trait, val in CHARACTERS[id]['traits'].items():
        character[trait] += (val / 100) * character[trait]

    return character
