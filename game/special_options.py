import game.item as it
import random

from opts import ROOMS, PREFABS
from game.game_manager import manager
from utils.functions import ask_int, pause, decide


def pet_cat(character):
    """Method for petting the cat

    Parameters
    ----------
    character : dict[str, Any]
        dictionary storing all the attributes of the character
    """
    manager['times_cat_pet'] += 1

    print("Cat meows")

    if manager['times_cat_pet'] == 4:
        print("Cat comes a little bit closer")

    elif manager['times_cat_pet'] == 7:
        print("Cat starts to purr")

    elif manager['times_cat_pet'] == 10:
        it.pick_items(PREFABS['cat_item'], 1, character)

    pause()


def play_piano(character):
    if manager['times_played_piano'] == 0:
        print("A piece fell down revealing a key", end="")
        pause()
        it.pick_items(PREFABS['basement_key'], 1, character)
        pause()
    else:
        print('You played the piano')
        if decide(25):
            print('A spider scared you and made you fall. You lost 2hp')
            character['hp'] -= 2
        pause()
    manager['times_played_piano'] += 1


def open_chest(character):
    """Method for opening the chest, show what is inside and options to get the items inside

    Parameters
    ----------
    character : dict[str, Any]
        dictionary storing all the attributes of the character
    """
    if len(ROOMS[character['room']['id']]['chest']) > 0:
        print("The chest contains:")

        for i, item in enumerate(ROOMS[character['room']['id']]['chest']):
            if item['type'] == 'weapon':
                print(
                    f"\t{i +1}- Name: {item['name']}, Quality: {item['quality']}, Strength: {item['traits']['strength']}")
            elif item['type'] == 'clothes':
                print(f"\t{i +1}- Name: {item['name']}, Quality: {item['quality']}, Sneak: {item['traits']['sneak']}")
            else:
                print(f"\t{i +1}- Name: {item['name']}, Quality: {item['quality']}, Shield: {item['traits']['shield']}")

        print()
        print(f"\t{i+2}- [Back]")
        print()

        result = ask_int(1, i+2)

        if result != i+2:
            win = ROOMS[character['room']['id']]['chest'][result-1]
            ROOMS[character['room']['id']]['chest'].remove(win)

            it.pick_items(win, 1, character)
    else:
        print('The chest is empty')
        pause()
    manager['character_displayed'] = False
    pass


def knife_poster(character):
    """Spooky message with spooky knife

    Parameters
    ----------
    character : dict[str, Any]
        dictionary storing all the attributes of the character
    """
    print('...', end="")
    pause()
    print('You find a poster with the image of your friends and a knife stabbed to it')
    pause()
    print('\t1- [Grab knife]\n\t2- [Leave]')
    print()

    if ask_int(1, 2) == 1:
        it.pick_items(PREFABS['kitchen_knife'], 1, character)
    else:
        ROOMS[character['room']['id']]['chest'].append(PREFABS['kitchen_knife'])


def get_toy(type, character):
    """Method for kids or adults who like to play with toys

    Parameters
    ----------
    type : string
        type of toy!
    character : dict[str, Any]
        dictionary storing all the attributes of the character
    """
    if type == 'train':
        print('You grab the train', end="")
        pause()
        if (random.random() > 0.5):
            print("A wheel fell off", end="")
        else:
            print("A rat scared you and the train fell on your feet", end="")
            pause()
            print('You took 5hp damage', end=" ")
            character['hp'] -= 5
        pause()

    if type == 'plushie':
        print('You squish the plushie and it makes some scary noise', end="")
        pause()
        print('You put it down', end="")
        pause()


def open(type, available, character):
    """Method for opening any drawer or cupboard

    Parameters
    ----------
    type : string
        type of furniture
    available : list
        list of possible items to generate
    character : dict[str, Any]
        dictionary storing all the attributes of the character
    """
    loot = None if random.random() < 0.55 else it.generate(available)
    print(f'You opened a {type}', end="")
    pause()
    if loot == None:
        print("You found nothing inside", end="")
    else:
        print(f"You have found an {loot['name']}")
        it.pick_items(loot, 1, character)
    pause()
    return None
