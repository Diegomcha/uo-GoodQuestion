# * GAME OPTIONS

KEYS = {
    'next': 'D',
    'previous': 'A',
    'select': 'S',
    'exit': 'E'
}
"""
Keys used.
"""

ACHIEVEMENTS_SAVE_PATH = "data.txt"
"""
Where to save the achievements progress.
"""

BASE_CHARACTERS = [
    {
        'name': 'SAM',
        'blood': 'AB+',
        'traits': {
            'swiftness': 1,
            'sneak': -1
        }
    },
    {
        'name': 'SARAH',
        'blood': '0-',
        'traits': {
            'strength': 1,
            'maxhp': -1
        }
    },
    {
        'name': 'CHRISTA',
        'blood': '0+',
        'traits': {
            'sneak': 1,
            'swiftness': -1
        }
    },
    {
        'name': 'MIKE',
        'blood': 'A+',
        'traits': {
            'maxhp': 1,
            'strength': -1
        }
    }
]
"""
Characters used in the game, new characters can be added and the structure is fixed except for the traits field which can have any number of traits (0-Inf).
"""

DIFFICULTIES = [
    {
        'name': 'Easy',
        'maxhp': 0,
        'strength': 0,
        'sneak': 0,
        'swiftness': 0,
        'remaining': 1
    },
    {
        'name': 'Medium',
        'maxhp': 0,
        'strength': 0,
        'sneak': 0,
        'swiftness': 0,
        'remaining': 1
    },
    {
        'name': 'Hard',
        'maxhp': 0,
        'strength': 0,
        'sneak': 0,
        'swiftness': 0,
        'remaining': 1
    }
]
"""
Base stats for each difficulty. New difficulties may be added, the structure is fixed though.
"""

QUALITIES = [
    {
        # id: 0
        'name': 'Legendary',
        'special': True,
        'rate': 5
    },
    {
        # id: 1
        'name': 'Rare',
        'special': False,
        'rate': 15
    },
    {
        # id: 2
        'name': 'Uncommon',
        'special': False,
        'rate': 30
    },
    {
        # id: 3
        'name': 'Common',
        'special': False,
        'rate': 50
    },
]
"""
List of all the available qualities.
"""

ITEMS = {
    'weapon': {
        'names': ['uwu'],
        'legendary_names': ['special'],
        'consumable': False,
        'pickable': True,
        'traits': [
            {
                # quality id: 0
                'strength': 4
            },
            {
                # quality id: 1
                'strength': 3
            },
            {
                # quality id: 2
                'strength': 2
            },
            {
                # quality id: 3
                'strength': 1
            }
        ]
    },
    'medicine': {
        'names': ['uwu'],
        'special_names': ['special'],
        'consumable': True,
        'pickable': True,
        'traits': [
            {
                # quality id: 0
                'strength': 4
            },
            {
                # quality id: 1
                'strength': 3
            },
            {
                # quality id: 2
                'strength': 2
            },
            {
                # quality id: 3
                'strength': 1
            }
        ]
    }
}
"""
List of the types of items.
"""

MONSTERS = [
]
"""
List of monsters.
"""

ROOMS = [
    {
        # id: 0
        'resemblance': 'entrance',
        'rates': {
            'item': 100,
            'monster': 0
        },
        'items': {
            'available': ['weapon', 'medicine'],
            'forced': []
        },
        'monsters': {
            'available': [],
            'forced': [],
            'base_stats': {

            }
        },
        'connections': [],
        'locked': None  # None or number of key
    },
    {
        # id: 1
        'resemblance': 'living room',
        'items': {

        }
    }
]
"""
List of rooms (Map of the house).
"""
