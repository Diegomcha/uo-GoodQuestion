from opts import MONSTER_SCALING, MONSTERS
from utils.functions import decide_index_rated_list, decide_list, round_traits


def generate(available, base, remaining):
    difficulty = 1 - ((remaining * MONSTER_SCALING) / 100)
    monster = {
        'type': decide_list(available) if type(available[0]) is str else available[decide_index_rated_list(available)]['type'],
        'hp': difficulty * base['maxhp'],
        'shield': 0,
        'strength': difficulty * base['strength'],
        'swiftness': difficulty * base['swiftness'],
        'flee': (1-difficulty) * base['flee']
    }

    monster['displayname'] = MONSTERS[monster['type']]['displayname']
    for trait, val in MONSTERS[monster['type']]['traits'].items():
        monster[trait] += (val/100) * monster[trait]

    monster = round_traits(monster, ['hp', 'strength'])

    return monster


def display(monster):
    print(f" · {monster['displayname']}")
    print(f"   - Health: {monster['hp']}")
    print(f"   - Strength: {monster['strength']}")


def display_combat(monster):
    print(f"{monster['displayname']}:")
    print(f" - Health: {monster['hp']}")
    print(f" - Strength: {monster['strength']}")
