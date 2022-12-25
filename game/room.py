from opts import ROOMS
from utils.functions import decide
import game.item as it


# Main methods
def display(room):
    print(f"You enter into a room that resembles a {room['resemblance']}.")

    if room['monster'] == room['item'] == None:
        print("You find nothing inside.")
    else:
        # TODO:
        # if room['monster'] != None:
        #     print(f"You find a monster!")
        #     print()
        if room['item'] != None:
            print(f"You find an item!")
            it.display(room['item'])
            print()


# Main
def generate(id, sneak):
    room = ROOMS[id]
    item_rate = room['rates']['item']
    monster_rate = room['rates']['monster'] - sneak

    item = None
    monster = None

    # generate item
    if item_rate > 0:
        if decide(item_rate):
            item = it.generate(room['items']['available'])
    # TODO: generate monster
    # if monster_rate > 0:
        # if decide(monster_rate):
            # monster = generate_monster(room['monsters']['available'], room['monsters']['base_stats'])

    return {
        'resemblance': room['resemblance'],
        'connections': room['connections'],
        'item': item,
        'monster': monster
    }
