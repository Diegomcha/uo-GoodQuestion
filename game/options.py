import game.room as rm
import game.character as char
import game.inventory_display as inv
import game.item as it
from game.options_logic import pick_items
from opts import ROOMS
from utils.functions import ask_int
from game.game_manager import manager
from game.options_logic import ask_if_continue



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
            pet_cat(character)

        elif special_options[selection] == "Play piano":
            play_piano()
            
        elif special_options[selection] == "item":
            pick_items(it.generate("weapon"),1,character)
            
        elif special_options[selection] == "Open chest":
            open_chest(character)

# TO-DO:


def pet_cat(character):
    manager['times_cat_pet'] += 1
    
    print("Cat meows")
    
    if manager['times_cat_pet'] == 4:
        print("Cat comes a little bit closer")
            
    elif manager['times_cat_pet'] == 7:
        print("Cat starts to purr")
        
    elif manager['times_cat_pet'] == 10:
        Cat_item = {'name': 'Miracolous cat gift', 'quality': 'Legendary', 'consumable': False, 'traits': [], 'type': 'faith_item', 'part_of_body': None}
        pick_items(Cat_item, 1, character)
    
    print()

def play_piano():
    print("A piece fell down revealing a key")
    
def open_chest(character):
    print("The chest contains:")
    
    for i, item in enumerate(ROOMS[character['room']['id']]['chest']):
        if item['type'] == 'weapon':
            print(f"\t{i +1}- Name: {item['name']}, Quality: {item['quality']}, Damage: {item['damage']}")
        else:
            print(f"\t{i +1}- Name: {item['name']}, Quality: {item['quality']}, Traits: {item['traits']}")
    print(f"\t{i+2}- [Back]")
    print()
    
    result = ask_int(1, i+2)
    
    if result != i+2:
        lose =character['inventory'][(ROOMS[character['room']['id']]['chest'])[result-1]['type']]
        win = ROOMS[character['room']['id']]['chest'][result-1]
        
        if ask_if_continue(lose, win, ROOMS[character['room']['id']]):
            ROOMS[character['room']['id']]['chest'].remove(win)
    pass
    # Item add key (index whatever)

# display([["Pet cat"], ["pick your nose"]])
