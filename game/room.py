import game.item as it
import game.room as rm

from opts import ROOMS
from utils.functions import decide, ask_int


# Main methods
def display(room, character):
    print(f"You enter into a room that resembles a {room['resemblance']}.")

    if not room['id'] in character['visited_rooms']:
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


def unlock(character, room):  
    if room['locked'] == None:
        return True
    
    for key in character['inventory']['keys']:    
        if key == room['locked']:
            character['inventory']['keys'].remove(key)
            room['locked'] = None
            return True
            
    return False



def move(character, room):
    print(f"----- {room['resemblance'].upper()} -----")
    print()
    print("Where to move?: ")
    print()

    for i, id in enumerate(room['connections']):
        print(f"{i+1} - Door {i+1} [{'????' if (id not in character['visited_rooms']) else ROOMS[id]['resemblance']}]")
    print(f"{len(room['connections']) +1 } - Exit")
    
    ask = ask_int(1, len(room['connections']) + 1)
    
    if( ask == len(room['connections']) + 1):
        return 0
    else:
        where_to = room['connections'][ask -1] 
        

    if unlock(character, ROOMS[where_to]):
        character['last_room'] = character['room']['id']
        character['visited_rooms'].append(character['room']['id'])
        character['room'] = rm.generate(where_to, character['sneak'])
        display(character['room'], character)
    else:
        print("Seems to be locked")


# Main
def generate(id, sneak):
    room = ROOMS[id]
    #item_rate = room['items']['rate']
    item_rate = 0
    # monster_rate = room['monsters']['rate'] - sneak

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
        'id': id,
        'resemblance': room['resemblance'],
        'connections': room['connections'],
        'item': item,
        'monster': monster
    }

