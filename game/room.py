import game.item as it

from opts import ROOMS
from utils.functions import decide, ask_int


# Main methods
def display(room):
    print(f"You enter into a room that resembles a {room['resemblance']}.")

    if room['monster'] == room['item'] == None:
        print("You find nothing inside.")
    else:
        if room['monster'] != None:
            print(f"You find a monster!")
            # TODO: monster display
            # mon.display(room['monster'])
            print()
        if room['item'] != None:
            print(f"You find an item!")
            it.display(room['item'])
            print()


def unlock(character, room):  # TODO: Change how the keys are stored
    return True if (room['locked'] == None) else (room['locked'] in character['inventory']['keys'])


def move(character, room):
    print(f"----- {room['resemblance'].upper()} -----")
    print()
    print("Where to move?: ")
    print()

    for i, connection in enumerate(room['conections']):
        print(f"\t{i} - {connection['resemblance']}")
    where_to = room['connections'][ask_int(1, len(room['conections']))-1]

    if unlock(where_to):
        character['room'] = where_to
    else:
        print("Seems to be locked")


# Main
def generate(id, sneak):
    room = ROOMS[id]
    item_rate = room['items']['rate']
    monster_rate = room['monsters']['rate'] - sneak

    item = None
    monster = None

    # generate item
    if item_rate > 0:
        if decide(item_rate):
            item = it.generate(room['items']['available'])
    if monster_rate > 0:
        if decide(monster_rate):
            # TODO: generate monster & remove pass
            pass
            # monster = mon.generate(room['monsters']['available'], room['monsters']['base_stats'])

    return {
        'resemblance': room['resemblance'],
        'connections': room['connections'],
        'item': item,
        'monster': monster
    }
