from utils.functions import ask_int
from opts import QUALITIES, ROOMS

def ask_if_continue(lose, win, room):
    if lose != None:
        print()
        print(f"Are you willing to change the {lose['type']} [Name: {lose['name']} - Quality: {QUALITIES[lose['quality']]['name']} - Traits: {lose['traits']}]")
        print(f"For the {win['type']} [Name: {win['name']} - Quality: {QUALITIES[win['quality']]['name']} - Traits: {win['traits']}]")
        print("""
            1 - [Yes]
            2 - [No]
            """)
        
        if ask_int(1,2) == 1:
            room['chest'].append(lose)
            return True
        else:
            room['chest'].append(win)
            return False
    else:
        return True
    
def pick_items(item, quantity, character):
    room = ROOMS[character['room']['id']]
    
    if item['type'] == 'key':
        character['inventory']['keys'].append(item['number'])
        
    elif item['type'] == 'clothes':
        if item['part_of_body'] == 'shirt' and ask_if_continue(character['inventory']['clothes']['shirt'], item, room):
            character['inventory']['clothes']['shirt'] == item
            print(f"You've received an {item['name']}")
            
        elif item['part_of_body'] == 'pants' and ask_if_continue(character['inventory']['clothes']['pants'], item, room):
            character['inventory']['clothes']['pants'] == item
            print(f"You've received an {item['name']}")
        
        elif item['part_of_body'] == 'shoes' and ask_if_continue(character['inventory']['clothes']['pants'], item, room):
            character['inventory']['clothes']['shoes'] == item
            print(f"You've received an {item['name']}")
        
        elif item['part_of_body'] == 'pijama' and ask_if_continue(character['inventory']['clothes']['shirt'], item, room) and ask_if_continue(character['inventory']['clothes']['pants'], item, room):
            character['inventory']['clothes']['shoes'] == item
            print(f"You've received an {item['name']}")
        
    elif item['type'] == 'medicine':
        for _ in range(quantity):
            character['inventory']['medicine'].append(item)
        print(f"You've received {quantity} {item['name']}{'s' if quantity > 1 else ''}")
        
    elif item['type'] == 'faith_item' and ask_if_continue(character['inventory']['faith_item'], item, room):
        character['inventory']['faith_item'] = item
        print(f"You've received an {item['name']}")

    elif item['type'] == 'weapon' and ask_if_continue(character['inventory']['weapon'], item, room):
        character['inventory']['weapon'] = item
        print(f"You've received an {item['name']}")