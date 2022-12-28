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
        'items': {
            'rate': 100,
            'available': ['weapon', 'medicine'],
            'forced': []
        },
        'monsters': {
            'rate': 0,
            'available': [],
            'forced': [],
            'base_stats': {

            }
        },
        'connections': [],
        'locked': None  # None or number of key
    }
]
"""
List of rooms (Map of the house).
"""

"""
List of achievements.
"""
ACHIEVEMENTS = {
"PACIFIST": ["PACIFIST", "Complete the game but no enemy was harmed during the proccess"],
"UNARMED" : ["UNARMED", "Complete the game without collecting any weapon"],
"SNEAKY PEAKY" : ["SNEAKY PEAKY", "Complete the game without finding an enemy (lucky you)"],
"ROOKIE TREASURE HUNTER" : ["ROOKIE TREASURE HUNTER", "Collect your first item"],
"ADVANCED TREASURE HUNTER" : ["ADVANCED TREASURE HUNTER", "Collect the halve of the items in one run"],
"GOD-LIKE TREASURE HUNTER" : ["GOD-LIKE-TREASURE HUNTER", "Collect all the items in one run"],
"SAVIOUR" : ["SAVIOUR", "Complete the game once"],
"MULTIPLE" : ["MULTIPLE", "Complete the game using all characters"],
"VOLATIN" : ["VOLATIN", "Save your mate and jump through the window to scape"],
"HERO" : ["HERO", "Defeat a total of 30 enemies in one run"]
}
