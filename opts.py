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

# Puse los traits en un dictionario asi no hay que poner todas las stats even if no hay changes
MONSTERS = [  # stats are provisional
    {
        'name': 'Ghoul',
        'traits': {
            'strength': 5,
            'swiftness': -5
        }
    },
    {
        'name': 'Giant rat',
        'traits': {
            'maxhp': 5,
            'strength': -5
        }
    },
    {
        'name': 'Viper',
        'traits': {
            'swiftness': 5
        }
    },
    {
        'name': 'Ghost',
        'traits': {}
    },
]
"""
List of monsters.
"""

ROOMS = [
    # Floor 0
    {
        # id: 0
        'special options' : ['Pet cat'],
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
        'connections': [1, 2, 3, 4, 5],
        'locked': None  # None or number of key
    },
    {
        # id: 1
        'resemblance': 'living room',
        # TODO: Add items and monster
        'connections': [0, 5],
        'locked': None  # None or number of key
    },
    {
        # id: 2
        'resemblance': 'kitchen',
        # TODO: Add items and monster
        'connections': [0, 3],
        'locked': None  # None or number of key
    },
    {
        # id: 3
        'resemblance': 'bathroom',
        # TODO: Add items and monster
        'connections': [0, 2],
        'locked': None  # None or number of key
    },
    {
        # id: 4
        'resemblance': 'stairs',
        # TODO: Add items and monster
        'connections': [0],
        'locked': None  # None or number of key
    },
    {
        # id: 5
        'resemblance': 'guests bedroom',
        # TODO: Add items and monster
        'connections': [0, 1],
        'locked': None  # None or number of key
    },
    # Floor 1
    {
        # id: 6
        'resemblance': 'hall2',
        # TODO: Add items and monster
        'connections': [4, 7, 8, 9, 10, 11, 12],
        'locked': None  # None or number of key
    },
    {
        # id: 7
        'resemblance': 'bathroom',
        # TODO: Add items and monster
        'connections': [6],
        'locked': None  # None or number of key
    }, {
        # id: 8
        'resemblance': 'diner',
        # TODO: Add items and monster
        'connections': [6],
        'locked': None  # None or number of key
    }, {
        # id: 9
        'resemblance': 'main bedroom',
        # TODO: Add items and monster
        'connections': [6, 12],
        'locked': None  # None or number of key
    }, {
        # id: 10
        'resemblance': 'bedroom',
        # TODO: Add items and monster
        'connections': [6],
        'locked': None  # None or number of key
    }, {
        # id: 11
        'resemblance': 'toys room',
        # TODO: Add items and monster
        'connections': [6],
        'locked': None  # None or number of key
    }, {
        # id: 12
        'resemblance': 'main bedroom bathroom',
        # TODO: Add items and monster
        'connections': [9],
        'locked': None  # None or number of key
    },
    # Floor 3
    {
        # id: 13
        'resemblance': 'atic',
        # TODO: Add items and monster
        'connections': [6],
        'locked': None  # None or number of key
    },
    # Basement
    {
        # id: 14
        'resemblance': 'basement',
        # TODO: Add items and monster
        'connections': [4],
        'locked': 1  # None or number of key
    }
]
"""
List of rooms (Map of the house).
"""

ACHIEVEMENTS = {
    "PACIFIST": ["PACIFIST", "Complete the game but no enemy was harmed during the proccess"],
    "UNARMED": ["UNARMED", "Complete the game without collecting any weapon"],
    "SNEAKY PEAKY": ["SNEAKY PEAKY", "Complete the game without finding an enemy (lucky you)"],
    "ROOKIE TREASURE HUNTER": ["ROOKIE TREASURE HUNTER", "Collect your first item"],
    "ADVANCED TREASURE HUNTER": ["ADVANCED TREASURE HUNTER", "Collect the halve of the items in one run"],
    "GOD-LIKE TREASURE HUNTER": ["GOD-LIKE-TREASURE HUNTER", "Collect all the items in one run"],
    "SAVIOUR": ["SAVIOUR", "Complete the game once"],
    "MULTIPLE": ["MULTIPLE", "Complete the game using all characters"],
    "VOLATIN": ["VOLATIN", "Save your mate and jump through the window to scape"],
    "HERO": ["HERO", "Defeat a total of 30 enemies in one run"]
}
"""
List of achievements.
"""
