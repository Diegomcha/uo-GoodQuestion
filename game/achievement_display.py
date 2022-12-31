import game.achievement_manager as am

from opts import KEYS, ACHIEVEMENTS_SAVE_PATH, ACHIEVEMENTS
from utils.functions import ask_options

TOTAL = len(ACHIEVEMENTS)


def paint(count, total, index, name_from_index, description):
    """ Makes the display of the achievement
    Args:
        count (int): total of achievements completed
        total (int): total of achievements available
        index (int): index of the achievement
        name_from_index (String): name of the achievement
        description (String): description of the achievement
    """
    print(f"----- ACHIEVEMENTS ({count} of {total} unlocked) -----")
    print()
    print(f"     {index + 1} - {name_from_index}")
    print(f"\t{description}")
    print()
    result = ask_options({
        KEYS['next']: 'Next',
        KEYS['previous']: 'Previous',
        KEYS['exit']: 'Exit'
    })

    if result == KEYS['next']:
        if index < count - 1:
            paint_logic(index+1)
        else:
            paint_logic(index)
    elif result == KEYS['previous']:
        if (index > 0):
            paint_logic(index - 1)
        else:
            paint_logic(index)
    elif result.upper == KEYS['exit']:
        return 1

    else:
        pass


def paint_logic(index_to_paint):
    """Gets the data for the paint method
    Args:
        index_to_paint (int): Index of the achievement you want to display
    """
    data = am.read_achievements(ACHIEVEMENTS_SAVE_PATH)
    count = len(data)
    name_from_index = am.separate_achievement(data[index_to_paint])[0]
    description = am.separate_achievement(data[index_to_paint])[1]

    paint(count, TOTAL, index_to_paint, name_from_index, description)


def display():
    paint_logic(0)
