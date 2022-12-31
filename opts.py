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

ACHIEVEMENTS_SAVE_PATH = "utils/assets/data.txt"
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
        'id': 0,
        'name': 'Legendary',
        'special': True,
        'rate': 5
    },
    {
        'id': 1,
        'name': 'Rare',
        'special': False,
        'rate': 15
    },
    {
        'id': 2,
        'name': 'Uncommon',
        'special': False,
        'rate': 30
    },
    {
        'id': 3,
        'name': 'Common',
        'special': False,
        'rate': 50
    },
]
"""
List of all the available qualities.
"""
SHIRTS_NAMES = []
PANTS_NAMES = []
SHOES_NAMES = []

ITEMS = {
    'weapon': {
        'names': ['knife', 'fork', 'machete', 'spike'],
        'legendary_names': ["cat's sword"],  # TODO: new names
        'consumable': False,
        'part_of_body': None,
        'duration': -1,
        'damage': None,
        'traits': [  # TODO: change rates
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
        'names': ['half-filled syringe', 'unknown pills', 'inhaler'],
        'special_names': ['glass of glowing liquid'],
        'consumable': True,
        'part_of_body': None,
        'duration': -1,
        'damage': None,
        'traits': [  # TODO: Change rates
            {
                # quality id: 0
                'hp': 4,
            },
            {
                # quality id: 1
                'hp': 3
            },
            {
                # quality id: 2
                'hp': 2
            },
            {
                # quality id: 3
                'hp': 1
            }
        ],
    },
    'clothes': {
        'names': ['broken t-shirt', 'shorts', 'sleepers'],
        'special_names': ['dino pijama'],
        'consumable': False,
        'part_of_body': ['shirt', 'pants', 'shoes', 'pijama'],
        'duration': -1,
        'damage': None,
        'traits': [  # TODO: Change rates
            {
                # quality id: 0
                'sneak': 4
            },
            {
                # quality id: 1
                'sneak': 3
            },
            {
                # quality id: 2
                'sneak': 2
            },
            {
                # quality id: 3
                'sneak': 1
            }
        ]
    },
    'energetic_drinks': {
        'names': ['PinkBull', 'NotMonster', 'Popstar', 'Freeze'],
        'special_names': ['Frosty Freezy Freeze'],
        'consumable': True,
        'duration': 1,
        'damage': None,
        'traits': [  # TODO: Change rates
            {
                # quality id: 0
                'swiftness': 4
            },
            {
                # quality id: 1
                'swiftness': 3
            },
            {
                # quality id: 2
                'swiftness': 2
            },
            {
                # quality id: 3
                'swiftness': 1
            }
        ]
    },
    'faith_item': {
        'names': ['wristband', 'cross', 'necklace', 'old watch'],
        'special_names': ["cat's necklace"],
        'consumable': False,
        'duration': -1,
        'damage': None,
        'traits': [  # TODO: Change rates
            {
                # quality id: 0
                'shield': 4
            },
            {
                # quality id: 1
                'shield': 3
            },
            {
                # quality id: 2
                'shield': 2
            },
            {
                # quality id: 3
                'shield': 1
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
        },
        'drop': [],
        'drop_rate': 0
        
    },
    {
        'name': 'Giant rat',
        'traits': {
            'maxhp': 5,
            'strength': -5
        },
        'drop': [],
        'drop_rate': 0
    },
    {
        'name': 'Viper',
        'traits': {
            'swiftness': 5
        },
        'drop': [],
        'drop_rate': 0
    },
    {
        'name': 'Ghost',
        'traits': {},
        'drop': [],
        'drop_rate': 0
    },
]
"""
List of monsters.
"""

ROOMS = [
    # Floor 0
    {
        # 'id': 0,
        'special_options': [],
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
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 1,
        'special_options': ['item'],
        'resemblance': 'living room',
        # TODO: Add items and monster
        'connections': [0, 5],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 2,
        'special_options': [],
        'resemblance': 'kitchen',
        # TODO: Add items and monster
        'connections': [0, 3],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 3,
        'special_options': ['item'],
        'resemblance': 'bathroom',
        # TODO: Add items and monster
        'connections': [0, 2],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 4,
        'special_options': [],
        'resemblance': 'stairs',
        # TODO: Add items and monster
        'connections': [0, 6, 14],
        'locked': None,  # None or number of key
        'chest': [1]
    },
    {
        # 'id': 5,
        'special_options': [],
        'resemblance': 'guests bedroom',
        # TODO: Add items and monster
        'connections': [0, 1],
        'locked': None,  # None or number of key
        'chest': []
    },
    # Floor 1
    {
        # 'id': 6,
        'special_options': [],
        'resemblance': 'hall',
        # TODO: Add items and monster
        'connections': [4, 7, 8, 9, 10, 11, 13],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 7,
        'special_options': [],
        'resemblance': 'bathroom',
        # TODO: Add items and monster
        'connections': [6],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 8,
        'special_options': [],
        'resemblance': 'diner',
        # TODO: Add items and monster
        'connections': [6],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 9,
        'special_options': [],
        'resemblance': 'main bedroom',
        # TODO: Add items and monster
        'connections': [6, 12],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 10,
        'special_options': [],
        'resemblance': 'bedroom',
        # TODO: Add items and monster
        'connections': [6],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 11,
        'special_options': [],
        'resemblance': 'toys room',
        # TODO: Add items and monster
        'connections': [6],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 12,
        'special_options': [],
        'resemblance': 'main bedroom bathroom',
        # TODO: Add items and monster
        'connections': [9],
        'locked': None,  # None or number of key
        'chest': []
    },
    # Floor 3
    {
        # 'id': 13,
        'special_options': [],
        'resemblance': 'atic',
        # TODO: Add items and monster
        'connections': [6],
        'locked': None,  # None or number of key
        'chest': []
    },
    # Basement
    {
        # 'id': 14,
        'special_options': ['cat'],
        'resemblance': 'basement',
        # TODO: Add items and monster
        'connections': [4],
        'locked': 1,  # None or number of key
        'chest': []
    }
]
"""
List of rooms (Map of the house).
"""

ACHIEVEMENTS = {
    "PACIFIST": ["PACIFIST", "Complete the game but no enemy was harmed during the proccess"],
    "UNARMED": ["UNARMED", "Complete the game without collecting any weapon"],
    "SNEAKY_PEAKY": ["SNEAKY PEAKY", "Complete the game without finding an enemy (lucky you)"],
    "ROOKIE_TREASURE_HUNTER": ["ROOKIE TREASURE HUNTER", "Collect your first item"],
    "ADVANCED_TREASURE_HUNTER": ["ADVANCED TREASURE HUNTER", "Collect the halve of the items in one run"],
    "GOD_LIKE_TREASURE_HUNTER": ["GOD-LIKE-TREASURE HUNTER", "Collect all the items in one run"],
    "SAVIOUR": ["SAVIOUR", "Complete the game once"],
    "GEORGE_OF_THE_JUNGLE": ["GEORGE OF THE JUNGLE", "Pet the cat 10 times and get his love"],
    "VOLATIN": ["VOLATIN", "Save your mate and jump through the window to scape"],
    "HERO": ["HERO", "Defeat a total of 30 enemies in one run"]
}
"""
List of achievements.
"""
TOTAL_TREASURES = 0


"""
    Other data
"""
