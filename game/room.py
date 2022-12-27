from opts import ROOMS
import character
from utils.functions import decide, ask_int
import game.item as it

actual_room = 0

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

def check_movable(room_to):
    if room_to['locked'] == None:
        return True
    else:
        if room_to['locked'] in character['inventory']['keys']:
            return True
        return False
            
def move(room):
    print(f"----- {room} -----")
    counter = 1
    print()
    print("Where to move?: ")
    print()
    for connection in room['conections']:
        print(f"\t{counter} - {connection['resemblance']}")
        counter += 1
    where_to = room['connections'][ask_int(1,len(room['conections']))-1]
    
    if check_movable(where_to):
        actual_room = where_to
    else:
        print("Seems to be locked")


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

