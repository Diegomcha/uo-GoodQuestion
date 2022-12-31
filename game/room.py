import game.item as it
import game.character as char

from opts import ROOMS
from utils.functions import decide, ask_int


# Main methods
def display(room, character):
    print(f"You enter into a room that resembles a {room['resemblance']}.")

    if room['monster'] != None:
        print(f"You find a monster!")
        # TODO: Display monster
        # mon.display(room['monster'])

    if room['id'] not in character['visited_rooms']:
        visit(room, character)

        if room['monster'] == room['item'] == None:
            print("You find nothing inside.")
        elif room['item'] != None:
            print(f"You find an item!")
            it.display(room['item'])


def visit(room, character):
    if room['id'] not in character['visited_rooms']:
        character['visited_rooms'].append(room['id'])


def generate(id, sneak):
    room = ROOMS[id]

    item = room['items']['custom']
    monster = room['monsters']['custom']

    item_rate = room['items']['rate'] if not item else 0
    monster_rate = (room['monsters']['rate'] - sneak) if not monster else 0

    # generate item
    if not item:
        if item_rate > 0:
            room['items']['rate'] = 0  # removes the possibility of an item appearing when the room has already been visited
            if decide(item_rate):  # if item is gonna be generated
                item = it.generate(room['items']['available'])
    else:
        room['items']['custom'] = None

    # TODO: generate monster
    if not monster and monster_rate > 0:
        if decide(monster_rate):
            # TODO: generate monster & remove pass
            pass
            # monster = mon.generate(room['monsters']['available'], room['monsters']['base_stats'])

    return {
        'id': id,
        'resemblance': room['resemblance'],
        'connections': room['connections'],
        'item': item,
        'monster': monster
    }
