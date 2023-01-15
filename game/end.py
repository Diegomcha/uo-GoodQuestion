import game.achievement_manager as am
from game.game_manager import manager
from opts import ACHIEVEMENTS_SAVE_PATH as path
from opts import ACHIEVEMENTS
import opts


def write_achivement():
    # If called, game completed
    am.write_achievement(path, ACHIEVEMENTS['SAVIOUR'])
    # ITEMS
    if manager['treasures_found'] > 0:
        am.write_achievement(path, ACHIEVEMENTS['ROOKIE_TREASURE_HUNTER'])
    if manager['treasures_found'] >= opts.TOTAL_TREASURES/2:
        am.write_achievement(path, ACHIEVEMENTS['ADVANCED_TREASURE_HUNTER'])
    if manager['treasures_found'] >= opts.TOTAL_TREASURES:
        am.write_achievement(path, ACHIEVEMENTS['GOD_LIKE_TREASURE_HUNTER'])
    # ENEMIES
    if manager['enemies_defeated'] == 0:
        am.write_achievement(path, ACHIEVEMENTS['PACIFIST'])
    if manager['enemies_defeated'] >= 30:
        am.write_achievement(path, ACHIEVEMENTS['HERO'])
    if manager['enemies_found'] == 0:
        am.write_achievement(path, ACHIEVEMENTS['SNEAKY_PEAKY'])
    # OTHERS
    if manager['times_cat_pet'] >= 10:
        am.write_achievement(path, ACHIEVEMENTS['GEORGE_OF_THE_JUNGLE'])
    if manager['weapons_taken'] == 0:
        am.write_achievement(path, ACHIEVEMENTS['UNARMED'])
    if manager['volatin']:
        am.write_achievement(path, ACHIEVEMENTS['VOLATIN'])
