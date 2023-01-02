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
        'maxhp': 120,
        'strength': 10,
        'sneak': 15,
        'swiftness': 25,
        'remaining': 50
    },
    {
        'name': 'Medium',
        'maxhp': 100,
        'strength': 8,
        'sneak': 10,
        'swiftness': 20,
        'remaining': 30
    },
    {
        'name': 'Hard',
        'maxhp': 80,
        'strength': 6,
        'sneak': 5,
        'swiftness': 10,
        'remaining': 15
    }
]
"""
Base stats for each difficulty. New difficulties may be added, the structure is fixed though.
"""

QUALITIES = [
    {
        'name': 'Legendary',
        'special': True,
        'rate': 5
    },
    {
        'name': 'Rare',
        'special': False,
        'rate': 15
    },
    {
        'name': 'Uncommon',
        'special': False,
        'rate': 30
    },
    {
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

BASE_DAMAGE_WEAPON = {'knife': 3, 'fork': 2, 'machete': 6, 'spike': 7, "cat's paw": 10}

ITEMS = {
    'weapon': {
        'names': ['knife', 'fork', 'machete', 'spike'],
        'special_names': ["cat's paw"],  # TODO: new names
        'consumable': False,
        'part_of_body': None,
        'duration': -1,
        'damage': None,
        'traits': [  # TODO: change rates
            {
                # quality id: 0
                'strength': 20
            },
            {
                # quality id: 1
                'strength': 10
            },
            {
                # quality id: 2
                'strength': 8
            },
            {
                # quality id: 3
                'strength': 5
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
                'hp': 30,
            },
            {
                # quality id: 1
                'hp': 20
            },
            {
                # quality id: 2
                'hp': 10
            },
            {
                # quality id: 3
                'hp': 5
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
                'sneak': 10
            },
            {
                # quality id: 1
                'sneak': 5
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
                'swiftness': 30
            },
            {
                # quality id: 1
                'swiftness': 15
            },
            {
                # quality id: 2
                'swiftness': 10
            },
            {
                # quality id: 3
                'swiftness': 5
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
                'shield': 10
            },
            {
                # quality id: 1
                'shield': 5
            },
            {
                # quality id: 2
                'shield': 3
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
MONSTERS = [  # stats are provisional and in percentages
    {
        'name': 'Ghoul',
        'traits': {
            'strength': 25,
            'swiftness': -40
        },
        'drop': [],
        'drop_rate': 0
    },
    {
        'name': 'Giant rat',
        'traits': {
            'maxhp': 50,
            'strength': -30
        },
        'drop': [],
        'drop_rate': 0
    },
    {
        'name': 'Viper',
        'traits': {
            'swiftness': 25
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
            'available': ['clothes'],
            'forced': None  # SOlo puede ser un item so no hace falta list
        },
        'monsters': {
            'rate': 0,
            'available': [],
            'forced': None,
            'base_stats': {}  # TODO: decide wether to use this aproach or not
        },
        'connections': [1, 2, 3, 4, 5],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 1,
        'special_options': ['item'],
        'resemblance': 'living room',
        'items': {
            'rate': 75,
            'available': [
                {
                    'type': 'clothes',
                    'rate': 70
                },
                {
                    'type': 'energetic_drinks',
                    'rate': 20
                },
                {
                    'type': 'weapon',
                    'rate': 10
                }
            ],
            'forced': None
        },
        'monsters': {
            'rate': 60,
            'available': [
                {
                    'type': 'ghoul',
                    'rate': 40
                },
                {
                    'type': 'giant_rat',
                    'rate': 50
                },
                {
                    'type': 'viper',
                    'rate': 10
                }
            ],
            'forced': None,
            'base_stats': {}  # TODO: decide whether to use this aproach or not
        },
        'connections': [0, 5],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 2,
        'special_options': ['Poster with a knife'],
        'resemblance': 'kitchen',
        'items': {
            'rate': 100,
            'available': ['weapon'],
            'forced': None
        },
        'monsters': {
            'rate': 75,
            'available': [
                {
                    'type': 'ghoul',
                    'rate': 10
                },
                {
                    'type': 'giant_rat',
                    'rate': 70
                },
                {
                    'type': 'viper',
                    'rate': 20
                }
            ],
            'forced': None
        },
        'connections': [0, 3],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 3,
        'special_options': ['Receive item'],
        'resemblance': 'bathroom',
        'items': {
            'rate': 100,
            'available': [
                {
                    'type': 'medicine',
                    'rate': 90
                },
                {
                    'type': 'weapon',
                    'rate': 10
                }
            ],
            'forced': None
        },
        'monsters': {
            'rate': 90,
            'available': [
                {
                    'type': 'giant_rat',
                    'rate': 60
                },
                {
                    'type': 'viper',
                    'rate': 40
                }
            ],
            'forced': None
        },
        'connections': [0, 2],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 4,
        'special_options': [],
        'resemblance': 'stairs',
        'items': {
            'rate': 25,
            'available': ['medicine'],
            'forced': None
        },
        'monsters': {
            'rate': 80,
            'available': [
                {
                    'type': 'giant_rat',
                    'rate': 55
                },
                {
                    'type': 'viper',
                    'rate': 45
                }
            ],
            'forced': None
        },
        'connections': [0, 6, 14],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 5,
        'special_options': [],
        'resemblance': 'guests bedroom',
        'items': {
            'rate': 100,
            'available': [
                {
                    'type': 'faith_item',
                    'rate': 30
                },
                {
                    'type': 'medicine',
                    'rate': 20
                },
                {
                    'type': 'clothes',
                    'rate': 50
                }
            ],
            'forced': None
        },
        'monsters': {
            'rate': 95,
            'available': [
                {
                    'type': 'ghoul',
                    'rate': 80
                },
                {
                    'type': 'viper',
                    'rate': 20
                }
            ],
            'forced': None
        },
        'connections': [0, 1],
        'locked': None,  # None or number of key
        'chest': []
    },
    # Floor 1
    {
        # 'id': 6,
        'special_options': ['Consume Item'],
        'resemblance': 'hall',
        'items': {
            'rate': 0,
            'forced': None
        },
        'monsters': {
            'rate': 100,
            'available': [
                {
                    'type': 'ghoul',
                    'rate': 80
                },
                {
                    'type': 'giant_rat',
                    'rate': 20
                },
                {
                    'type': 'viper',
                    'rate': 10
                }
            ],
            'forced': None
        },
        'connections': [4, 7, 8, 9, 10, 11, 13],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 7,
        'special_options': [],
        'resemblance': 'bathroom',
        'items': {
            'rate': 90,
            'available': [
                {
                    'type': 'medicine',
                    'rate': 90
                },
                {
                    'type': 'weapon',
                    'rate': 10
                }
            ],
            'forced': None
        },
        'monsters': {
            'rate': 100,
            'available': [
                {
                    'type': 'ghoul',
                    'rate': 10
                },
                {
                    'type': 'giant_rat',
                    'rate': 60
                },
                {
                    'type': 'viper',
                    'rate': 30
                }
            ],
            'forced': None
        },
        'connections': [6],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 8,
        'special_options': [],
        'resemblance': 'diner',
        'items': {
            'forced': None  # TODO: Here the key to the basement
            # {
            #     'name': 'key',
            #     'type': 'key',
            #     'id': 1
            # }
        },
        'monsters': {
            'rate': 100,
            'available': [
                {
                    'type': 'ghoul',
                    'rate': 10
                },
                {
                    'type': 'giant_rat',
                    'rate': 60
                },
                {
                    'type': 'viper',
                    'rate': 30
                }
            ],
            'forced': None
        },
        'connections': [6],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 9,
        'special_options': ['Play piano'],
        'resemblance': 'main bedroom',
        'items': {
            'rate': 100,
            'available': [
                {
                    'type': 'clothes',
                    'rate': 70
                },
                {
                    'type': 'medicine',
                    'rate': 25
                },
                {
                    'type': 'faith_item',
                    'rate': 5
                }
            ],
            'forced': None
        },
        'monsters': {
            'rate': 100,
            'available': [
                {
                    'type': 'ghoul',
                    'rate': 70
                },
                {
                    'type': 'viper',
                    'rate': 30
                }
            ],
            'forced': None
        },
        'connections': [6, 12],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 10,
        'special_options': [],
        'resemblance': 'bedroom',
        'items': {
            'rate': 80,
            'available': [
                {
                    'type': 'clothes',
                    'rate': 70
                },
                {
                    'type': 'medicine',
                    'rate': 30
                }
            ],
            'forced': None
        },
        'monsters': {
            'rate': 100,
            'available': [
                {
                    'type': 'ghoul',
                    'rate': 25
                },
                {
                    'type': 'giant_rat',
                    'rate': 25
                },
                {
                    'type': 'viper',
                    'rate': 50
                }
            ],
            'forced': None
        },
        'connections': [6],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 11,
        'special_options': ['Get a train toy', 'Get a plushie', 'Open drawner'],
        'resemblance': 'toys room',
        'items': {
            'forced': None  # TODO: Here the key to the attic
            # {
            #     'name': 'stick',
            #     'type': 'key',
            #     'id': 0
            # }
        },
        'monsters': {
            'rate': 100,
            'available': [
                {
                    'type': 'ghoul',
                    'rate': 30
                },
                {
                    'type': 'viper',
                    'rate': 70
                }
            ],
            'forced': None
        },
        'connections': [6],
        'locked': None,  # None or number of key
        'chest': []
    },
    {
        # 'id': 12,
        'special_options': [],
        'resemblance': 'main bedroom bathroom',
        'items': {
            'rate': 100,
            'available': [
                {
                    'type': 'medicine',
                    'rate': 90
                },
                {
                    'type': 'weapon',
                    'rate': 5
                },
                {
                    'type': 'faith_item',
                    'rate': 5
                }
            ],
            'forced': None

        },
        'monsters': {
            'rate': 100,
            'available': [
                {
                    'type': 'ghoul',
                    'rate': 40
                },
                {
                    'type': 'viper',
                    'rate': 60
                }
            ],
            'forced': None
        },
        'connections': [9],
        'locked': None,  # None or number of key
        'chest': []
    },
    # Floor 3
    {
        # 'id': 13,
        'special_options': ['friend', 'window'],
        'resemblance': 'atic',
        # TODO: Add items and monster
        'connections': [6],
        'locked': None,  # None or number of key
        'chest': []
    },
    # Basement
    {
        # 'id': 14,
        'special_options': ['Play with cat'],
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
PREFABS = {

    'Boots_of_the_swiftness_of_a_cat':
        {
            'type': 'clothes',
            'name': 'Boots of the swiftness of a cat',
            'quality': 4,
            'consumable': False,
            'damage': None,
            'part_of_body': 'shoes',
            'traits': []
        },
    'kitchen_knife':
        {
            'type': 'weapon',
            'name': 'Kitchen knife',
            'quality': 2,
            'consumable': False,
            'damage': 5.5,
            'part_of_body': None,
            'traits': []
        },
    'cat_item':
        {
            'type': 'faith_item',
            'name': 'Miracolous cat gift',
            'quality': 4,
            'consumable': False,
            'damage': None,
            'part_of_body': None,
            'traits': []
        }
}

FRIEND = {
    'name': 'Ian',
    'locked': 13,
    'item': [PREFABS['Boots_of_the_swiftness_of_a_cat']]


}
TOTAL_TREASURES = 0

"""
    Other data
"""
