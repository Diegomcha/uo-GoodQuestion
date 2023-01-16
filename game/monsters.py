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
    monsterinfo = MONSTERS[monster_type_to_id[available[decide_index_rated_list(available)]['type']]]

    monster = {
        'name': monsterinfo['display_name'],
        'maxhp': monsterinfo['maxhp'],
        'strength': monsterinfo['strength'],
        'swiftness': monsterinfo['swiftness'],
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
        ghost['escape_rate'] = 50
        if elo > 150 and decide(25):
            ghost['category'] = 'Special'

    elif difficulty == 'Medium':
        ghost['escape_rate'] = 33
        if elo > 130 and decide(33):
            ghost['category'] = 'Special'

    elif difficulty == 'Hard':
        ghost['escape_rate'] = 25
        if elo > 90 and decide(50):
            ghost['category'] = 'Special'

    return {
        **ghost,  # spread operator used to unpack the dictionary into the new one
        'maxhp': monster['maxhp'] if ghost['category'] == 'Special' else round(0.75*monster['maxhp']),
        'hp': monster['maxhp'] if ghost['category'] == 'Special' else round(0.75*monster['maxhp']),
        'strength': monster['strength'] if ghost['category'] == 'Special' else round(0.75*monster['strength'])
    }
