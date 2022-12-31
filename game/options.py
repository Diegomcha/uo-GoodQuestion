import game.room as rm
import game.character as char
import game.inventory_display as inv
from utils.functions import ask_if_continue
import game.item as it
from opts import ROOMS

from utils.functions import ask_int


# special_options = [option1.....]
def print_special_options(special_options):
    for i, element in enumerate(special_options):
        print(f"{i+3} - [{element}]")
    return len(special_options)


def display(special_options, character):
       
    if len(ROOMS[character['room']['id']]['chest']) != 0:
        if 'Open chest' not in ROOMS[character['room']['id']]['special_options']:
            ROOMS[character['room']['id']]['special_options'].append('Open chest')
            display(ROOMS[character['room']['id']]['special_options'], character)
            
    # print("----- OPTIONS -----")
    # print()
    print("1 - [Go to another room]")
    print("2 - [Check inventory]")
        
    new_options = print_special_options(special_options)
    print()
    selection = ask_int(1, 2 + new_options)

    if selection == 1:
        rm.move(character, character['room'])
        display(ROOMS[character['room']['id']]['special_options'], character)
    elif selection == 2:
        inv.display_inventory(character)
        input()
        char.display(character)
    else:
        selection -= 3
        if special_options[selection] == "cat":
            pet_cat()

        elif special_options[selection] == "Play piano":
            play_piano()
            
        elif special_options[selection] == "item":
            get_item(it.generate(['medicine']),1,character)
            
        elif special_options[selection] == "Open chest":
            open_chest(character)

# TO-DO:
def get_item(item, quantity, character):
    room = ROOMS[character['room']['id']]
    
    if item['type'] == 'key':
        character['inventory']['keys'].append(item)
        
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

def pet_cat():
    print("Miau")


def play_piano():
    print("A piece fell down revealing a key")
    
def open_chest(character):
    print(ROOMS[character['room']['id']]['chest'])
    # Item add key (index whatever)

# display([["Pet cat"], ["pick your nose"]])
