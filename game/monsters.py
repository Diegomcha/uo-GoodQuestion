from utils.functions import decide_index_rated_list, decide
from opts import MONSTERS
import random


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

    monster_info = MONSTERS[available[decide_index_rated_list(available)]['type']]
    monster = {
        'name': monster_info['display_name'],
        'maxhp': monster_info['maxhp'],
        'strength': monster_info['strength'],
        'swiftness': monster_info['swiftness'],
        'category': 'Basic'
    }

    if difficulty == 'Easy':
        monster['escape_rate'] = 50
        if elo > 150 and decide(25):
            monster['strength'] += random.randint(1, 8)
            monster['maxhp'] += random.randint(10, 20)
            monster['category'] = 'Special'

    elif difficulty == 'Medium':
        monster['escape_rate'] = 33
        if elo > 130 and decide(33):
            monster['strength'] += random.randint(1, 9)
            monster['maxhp'] += random.randint(10, 20)
            monster['category'] = 'Special'

    elif difficulty == 'Hard':
        monster['escape_rate'] = 25
        if elo > 90 and decide(50):
            monster['strength'] += random.randint(1, 10)
            monster['maxhp'] += random.randint(10, 30)
            monster['category'] = 'Special'

    monster['hp'] = monster['maxhp']
    return monster


def generate_ghost(monster, difficulty, elo):
    ghost = {
        'name': 'Ghost',
        'category': 'Basic',
        'swiftness': 0
    }

    if difficulty == 'Easy':
        if elo > 150 and decide(25):
            ghost['category'] = 'Special'

    elif difficulty == 'Medium':
        if elo > 130 and decide(33):
            ghost['category'] = 'Special'

    elif difficulty == 'Hard':
        if elo > 90 and decide(50):
            ghost['category'] = 'Special'

    ghost['escape_rate'] = monster['escape_rate']
    ghost['maxhp'] = monster['maxhp'] if ghost['category'] == 'Special' else round(0.75*monster['maxhp'])
    ghost['hp'] = monster['maxhp'] if ghost['category'] == 'Special' else round(0.75*monster['maxhp'])
    ghost['strength'] = monster['strength'] if ghost['category'] == 'Special' else round(0.75*monster['strength'])
    return ghost
