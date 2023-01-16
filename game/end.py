import game.achievement_manager as am
from game.game_manager import manager
from opts import ACHIEVEMENTS_SAVE_PATH as path
from opts import ACHIEVEMENTS
from utils.functions import pause, ask_int
import opts


def write_achivements():
    """Method that checks the data stored by the manager and writes the different achivements to the 'data.txt' file
    """
    # If called, game completed
    if manager['good_ending']:
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
    else:
        am.write_achievement(path, ACHIEVEMENTS['THE_BAD_DECISION'])


def ending(character):
    print('\'You finally reached the attic, you finally found your friend.\'')
    pause('...')
    print(f"Ian: {character['name']}! You were right, I should not have entered, it was like a nightmare. Lets get out of here please...")
    pause('...')
    print('\'You suddenly heard a noise, something seems to be crawling in the floor below, it seems its a good moment to leave this place.\'')
    pause('...')
    print('\'You thought to yourself and concluded there are only two options,\'')
    print('\t(1) You think to yourself about jumping through the attic window, although its risky you might survive. Your mate seems prepared to jump.')
    pause()
    print('\t(2) Your other option is to run down to the exit as fast as you can, you better pray you´ve got enough time before whatever is below finds you!')
    pause('...')
    print('\tWhat will be your decision?')
    pause()
    print('\t1 - [Jump through the window]\t')
    pause("")
    print('\t2 - [Run down to the exit]')

    result = ask_int(1, 2)

    if result == 1:
        manager['volatin'] = True

    if result == 2:
        character['remaining'] -= 5
        if character['remaining'] <= 0:
            print("\'As you reached the exit you felt as if something dragged you in again, at that moment you realized your friend was no longer with you.\'")
            pause('...')
            print("\'While being held, you raised your head just to realize the grotesque apareance of the creature that was , your friend laid behind it. It seems he got him first.\'")
            print("\'Then and there you came to the conclusion that the noises from earlier where made by that thing and before you could do anything else it brutally murdered you.\'")
            pause('...')
            print("\'You slowly began to loose your sight when suddenly you heard your friends voice one final time.\'")
            pause('...')
            print("Ian: You know, maybe it was a bad decision to come here after all...")
        else:
            print("As you ran to the exit you felt something chasing you, without looking behind you managed to escape, your friend left ")
    write_achivements()
