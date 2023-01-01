import game.item as it
import game.monster as mon

from opts import ROOMS
from utils.functions import decide


# Main methods
def display(room, character):
    print(f"You enter into a room that resembles a {room['resemblance']}.")

    if room['monster'] != None:
        print(f"You find a monster!")
        mon.display(room['monster'])
    elif room['id'] not in character['visited_rooms']:
        visit(room, character)

        if room['monster'] == room['item'] == None:
            print("You find nothing inside.")
        else:
            display_item(room)


def display_item(room):
    if room['item'] != None:
        print(f"You find an item!")
        it.display(room['item'])


def visit(room, character):
    if room['id'] not in character['visited_rooms']:
        character['visited_rooms'].append(room['id'])


def generate(id, character):
    room = ROOMS[id]

    item = room['items']['custom']
    monster = room['monsters']['custom']

    item_rate = room['items']['rate'] if not item else 0
    monster_rate = (room['monsters']['rate'] - character['sneak']) if not monster else 0

    # generate item
    if not item:
        if item_rate > 0:
            room['items']['rate'] = 0  # removes the possibility of an item appearing when the room has already been visited
            if decide(item_rate):  # if item is gonna be generated
                item = it.generate(room['items']['available'])
    else:
        room['items']['custom'] = None

    if not monster and monster_rate > 0:
        if decide(monster_rate):
            monster = mon.generate(room['monsters']['available'], character['monster_base'], character['remaining'])

    return {
        'id': id,
        'resemblance': room['resemblance'],
        'connections': room['connections'],
        'item': item,
        'monster': monster
    }
