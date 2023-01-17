import game.achievement_manager as am

from opts import KEYS, ACHIEVEMENTS_SAVE_PATH, ACHIEVEMENTS
from utils.functions import ask_options

TOTAL = len(ACHIEVEMENTS)


def paint(count, total, index, name_from_index, description):
    """ Makes the display of the achievement

    Parameters
    ----------
        count : int
            Total of achievements completed
        total : int
            Total of achievements available
        index : int: 
            Index of the achievement
        name_from_index : str
            Name of the achievement
        description : str
            Description of the achievement
    """
    print(f"----- ACHIEVEMENTS ({count} of {total} unlocked) -----")
    print()

    if index != -1:
        print(f"     {index+1} - {name_from_index}")
        print(f"\t{description}")
        print()
        result = ask_options({
            KEYS['next']: 'Next',
            KEYS['previous']: 'Previous',
            KEYS['exit']: 'Exit'
        })
    else:
        result = ask_options({
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
    elif result == KEYS['exit']:
        return None

    else:
        pass


def paint_logic(index_to_paint):
    """Gets the data for the paint method

    Parameters:
    ----------
        index_to_paint : int
            Index of the achievement you want to display
    """
    data = am.read_achievements(ACHIEVEMENTS_SAVE_PATH)
    count = len(data)
    if count == 0:
        paint(count, TOTAL, -1, "", "")
        return None
    name_from_index = am.separate_achievement(data[index_to_paint])[0]
    description = am.separate_achievement(data[index_to_paint])[1].rstrip()

    paint(count, TOTAL, index_to_paint, name_from_index, description)


def display():
    paint_logic(0)
