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
            'swiftness': 50,
            'sneak': -25
        }
    },
    {
        'name': 'SARAH',
        'blood': '0-',
        'traits': {
            'strength': 60,
            'maxhp': -40
        }
    },
    {
        'name': 'CHRISTA',
        'blood': '0+',
        'traits': {
            'sneak': 50,
            'swiftness': -25
        }
    },
    {
        'name': 'MIKE',
        'blood': 'A+',
        'traits': {
            'maxhp': 75,
            'strength': -50
        }
    }
]
"""
Characters used in the game, new characters can be added and the structure is fixed except for the traits field which can have any number of traits (0-Inf).
"""

DIFFICULTIES = [
    {
        'name': 'Easy',
        'moves': 40,
        'maxhp': 30,
        'strength': 10,
        'sneak': 10,
        'swiftness': 10,
        'flee': 90
    },
    {
        'name': 'Medium',
        'moves': 24,
        'maxhp': 30,
        'strength': 8,
        'sneak': 8,
        'swiftness': 8,
        'flee': 70
    },
    {
        'name': 'Hard',
        'moves': 12,
        'maxhp': 20,
        'strength': 5,
        'sneak': 1,
        'swiftness': 1,
        'flee': 30
    }
]
"""
Base stats for each difficulty. New difficulties may be added, the structure is fixed though.
"""

QUALITIES = [
    {
        'name': 'Legendary',
        'special': True,  # Special qualities use special_names and its effects / traits are unbounded
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

INVENTORY_SIZE = 3

ITEMS = {
    'weapon': {
        'names': ['knife', 'fork', 'machete', 'spike'],
        'special_names': ["Maxwell's sword"],
        'consumable': False,
        'duration': -1,
        'traits': [
            {
                # quality id: 0
                'strength': 10
            },
            {
                # quality id: 1
                'strength': 5
            },
            {
                # quality id: 2
                'strength': 3
            },
            {
                # quality id: 3
                'strength': 1
            }
        ]
    },
    'medicine': {
        'names': ['half-filled syringe', 'unknown pills', 'inhaler'],
        'special_names': ['Glowing Liquid filled bottle'],
        'consumable': True,
        'duration': -1,
        'traits': [
            {
                # quality id: 0
                'hp': 10
            },
            {
                # quality id: 1
                'hp': 5
            },
            {
                # quality id: 2
                'hp': 4
            },
            {
                # quality id: 3
                'hp': 3
            }
        ],
    },
    'clothing': {
        'names': ['broken t-shirt', 'shorts', 'sleepers'],
        'special_names': ['Dino Pijama'],
        'consumable': False,
        'duration': -1,
        'traits': [
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
    'energetic_drink': {
        'names': ['PinkBull', 'NotMonster', 'Popstar', 'Freeze'],
        'special_names': ['Frosty Freezy Freeze'],
        'consumable': True,
        'duration': 1,
        'traits': [
            {
                # quality id: 0
                'swiftness': 50
            },
            {
                # quality id: 1
                'swiftness': 30
            },
            {
                # quality id: 2
                'swiftness': 15
            },
            {
                # quality id: 3
                'swiftness': 5
            }
        ]
    },
    'faith_shield': {
        'names': ['wristband', 'cross', 'necklace', 'old watch'],
        'special_names': ["cat's necklace"],
        'consumable': False,
        'duration': -1,
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

MONSTER_SCALING = 2.25
"""
Percentage that monster use to scale.
"""

MONSTERS = {
    'ghoul': {
        'displayname': 'Ghoul',
        'traits': {
            'strength': 25,
            'swiftness': 40
        }
    },
    'giant_rat': {
        'displayname': 'Giant rat',
        'traits': {
            'hp': 50,
            'strength': -30
        }
    },
    'viper': {
        'displayname': 'Viper',
        'traits': {
            'swiftness': 25
        }
    }
}
"""
List of monsters.
"""

ROOMS = [
    # Floor 0
    {
        # id: 0
        'resemblance': 'entrance',
        'items': {
            'rate': 100,
            'available': ['clothing'],
            'custom': None
        },
        'monsters': {
            'rate': 10,
            'available': ['ghoul', 'giant_rat'],
            'custom': None
        },
        'connections': [1, 2, 3, 4, 5],
        'locked': None
    },
    {
        # id: 1
        'resemblance': 'living room',
        'items': {
            'rate': 75,
            'available': [
                {
                    'type': 'clothing',
                    'rate': 70
                },
                {
                    'type': 'energetic_drink',
                    'rate': 20
                },
                {
                    'type': 'weapon',
                    'rate': 10
                }
            ],
            'custom': None
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
            'custom': None
        },
        'connections': [0, 5],
        'locked': None
    },
    {
        # id: 2
        'resemblance': 'kitchen',
        'items': {
            'rate': 100,
            'available': ['weapon'],
            'custom': None
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
            'custom': None
        },
        'connections': [0, 3],
        'locked': None  # None or number of key
    },
    {
        # 'id': 3,
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
            'custom': None
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
            'custom': None
        },
        'connections': [0, 2],
        'locked': None  # None or number of key
    },
    {
        # 'id': 4,
        'resemblance': 'stairs',
        'items': {
            'rate': 25,
            'available': ['medicine'],
            'custom': None
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
            'custom': None
        },
        'connections': [0, 6, 14],
        'locked': None  # None or number of key
    },
    {
        # 'id': 5,
        'resemblance': 'guests bedroom',
        'items': {
            'rate': 100,
            'available': [
                {
                    'type': 'faith_shield',
                    'rate': 30
                },
                {
                    'type': 'medicine',
                    'rate': 20
                },
                {
                    'type': 'clothing',
                    'rate': 50
                }
            ],
            'custom': None
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
            'custom': None
        },
        'connections': [0, 1],
        'locked': None  # None or number of key
    },
    # Floor 1
    {
        # 'id': 6,
        'resemblance': 'hall',
        'items': {
            'rate': 0,
            'custom': None
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
            'custom': None
        },
        'connections': [4, 7, 8, 9, 10, 11, 12, 13],
        'locked': None  # None or number of key
    },
    {
        # 'id': 7,
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
            'custom': None
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
            'custom': None
        },
        'connections': [6],
        'locked': None  # None or number of key
    },
    {
        # 'id': 8,
        'resemblance': 'diner',
        'items': {
            'custom': {
                'name': 'key',
                'type': 'key',
                'id': 1
            }
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
            'custom': None
        },
        'connections': [6],
        'locked': None  # None or number of key
    },
    {
        # 'id': 9,
        'resemblance': 'main bedroom',
        'items': {
            'rate': 100,
            'available': [
                {
                    'type': 'clothing',
                    'rate': 70
                },
                {
                    'type': 'medicine',
                    'rate': 25
                },
                {
                    'type': 'faith_shield',
                    'rate': 5
                }
            ],
            'custom': None
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
            'custom': None
        },
        'connections': [6, 12],
        'locked': None  # None or number of key
    },
    {
        # 'id': 10,
        'resemblance': 'bedroom',
        'items': {
            'rate': 80,
            'available': [
                {
                    'type': 'clothing',
                    'rate': 70
                },
                {
                    'type': 'medicine',
                    'rate': 30
                }
            ],
            'custom': None
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
            'custom': None
        },
        'connections': [6],
        'locked': None  # None or number of key
    },
    {
        # 'id': 11,
        'resemblance': 'toys room',
        'items': {
            'custom': {
                'name': 'stick',
                'type': 'key',
                'id': 0
            }
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
            'custom': None
        },
        'connections': [6],
        'locked': None  # None or number of key
    },
    {
        # 'id': 12,
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
                    'rate': 5
                },
                {
                    'type': 'faith_shield',
                    'rate': 5
                }
            ],
            'custom': None

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
            'custom': None
        },
        'connections': [9],
        'locked': None  # None or number of key
    },
    # Floor 3
    {
        # 'id': 13,
        'resemblance': 'atic',
        # TODO: Add items and monster
        'connections': [6],
        'locked': 0  # None or number of key
    },
    # Basement
    {
        # 'id': 14,
        'resemblance': 'basement',
        'items': {
            'custom': {
                'name': 'Maxwell the cat',
                'special': True,
                'quality': 0,
                'type': 'cat',
                'consumable': False,
                'traits': {
                    'shield': 100,
                    'strength': 100,
                    'swiftness': 100
                }
            }
        },
        'monsters': {
            'rate': 0,
            'custom': None  # TODO: maybe add a monster or something
        },
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
