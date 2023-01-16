from utils.functions import decide_index_rated_list
from opts import MONSTERS
import random

monster_type_to_id = {'ghoul': 0, 'giant_rat': 1, 'viper': 2, 'ghost': 3}


def generate(available, difficulty, elo):
    """Method for generating a monster having in mind the difficulty chosen and the player power

    Parameters
    ----------
    available : list
        list containing the type of monsters to generate
    difficulty : string
        name of the local difficulty
    elo : int
        power of the character

    Returns
    -------
    dict[str, Any]
        dictionary containing the attributes of the monster
    """
    monsterinfo = MONSTERS[monster_type_to_id[available[decide_index_rated_list(available)]['type']]]

    monster = {
        'name': monsterinfo['name'],
        'hp': monsterinfo['maxhp'],
        'maxhp': monsterinfo['maxhp'],
        'strength': monsterinfo['strength'],
        'swiftness': monsterinfo['swiftness'],
        'category': monsterinfo['category']
    }
    if difficulty == 'Easy':
        monster['scape_rate'] = 50
        if elo > 150 and random.randint(1, 4) == 1:
            monster['strength'] += random.randint(1, 8)
            monster['hp'] += random.randint(10, 20)
            monster['category'] = 'Special'

    elif difficulty == 'Medium':
        monster['scape_rate'] = 33
        if elo > 130 and random.randint(1, 3) == 1:
            monster['strength'] += random.randint(1, 9)
            monster['hp'] += random.randint(10, 20)
            monster['category'] = 'Special'

    elif difficulty == 'Hard':
        monster['scape_rate'] = 25
        if elo > 90 and random.randint(1, 2) == 1:
            monster['strength'] += random.randint(1, 10)
            monster['hp'] += random.randint(10, 30)
            monster['category'] = 'Special'

    return monster
