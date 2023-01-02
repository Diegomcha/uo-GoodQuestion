import game.item as it
import game.character as char
from game.game_manager import manager

from opts import ROOMS
from utils.functions import decide, ask_int


# Main methods
def display(room, character):

    if not room['id'] in character['visited_rooms']:
        print(f"You enter into a room that resembles a {room['resemblance']}")
        
        manager['rooms_visited'].append(room)
        
        if room['resemblance'] != 'stairs':
            if room['monster'] == room['item'] == None:
                print("You find nothing inside.", end="")
                input()
            else:
                if room['monster'] != None:
                    print(f"You find a monster!", end="")
                    # TODO: Display monster
                    # mon.display(room['monster'])
                    print()
                if room['item'] != None:
                    it.pick_items(room['item'], 1, character)
                
    else:
        print(f"You return to the {room['resemblance']}.", end = "")
        input()


def unlock(character, room):
    if room['locked'] == None:
        return True


    if room['locked'] in character['inventory']['keys']:
        character['inventory']['keys'].remove(room['locked'])
        room['locked'] = None
        print('You unlock the door with the key you have in your inventory.')
        return True

    return False


def move(character, room):
    print(f"----- {room['resemblance'].upper()} -----")
    print()

    for i, id in enumerate(room['connections']):
        print(f"{i+1} - Door {i+1} [{'????' if (id not in character['visited_rooms']) else ROOMS[id]['resemblance']}]")
    print(f"{len(room['connections']) +1 } - Back")
    print()

    ask = ask_int(1, len(room['connections']) + 1)

    if (ask == len(room['connections']) + 1):
        return 0
    else:
        where_to = room['connections'][ask - 1]

    if unlock(character, ROOMS[where_to]):
        character['last_room'] = character['room']['id']
        character['visited_rooms'].append(character['room']['id'])
        character['room'] = generate(where_to, character['sneak'], character['difficulty'])
        char.display(character)
        manager['character_displayed'] = True
        display(character['room'], character)
    else:
        print("Seems to be locked")


# Main
def generate(id, sneak, difficulty):
    room = ROOMS[id]
    try:
        item_rate = room['items']['rate'] * 0.5 if difficulty == 2 else room['items']['rate'] * 0.8 if difficulty == 1 else room['items']['rate']
        monster_rate = room['monsters']['rate'] - sneak
    except:
        pass

    item = None
    monster = None

    # generate item
    try:
        if item_rate > 0:
            room['items']['rate'] = 0  # removes the possibility of an item appearing when the room has already been visited
            if decide(item_rate):  # if item is gonna be generated
                item = it.generate(room['items']['available'], room['items']['max_quality'])
    except:
        pass

    # TODO: generate monster
    try:
        if monster_rate > 0:
            if decide(monster_rate):
                # TODO: generate monster & remove pass
                pass
                # monster = mon.generate(room['monsters']['available'], room['monsters']['base_stats'])
    except:
        pass

    return {
        'id': id,
        'resemblance': room['resemblance'],
        'connections': room['connections'],
        'item': item,
        'monster': monster
    }
