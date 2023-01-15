import game.character as char
import game.item as it 
import game.special_options as so
import game.character as char

from opts import ROOMS
from game.game_manager import manager
from utils.functions import ask_int



# special_options = [option1.....]
def print_special_options(special_options):
    for i, element in enumerate(special_options):
        print(f"{i+3} - [{element}]")
    return len(special_options)


def display(special_options, character):
    
    if not manager['character_displayed']:
        print()
        char.display(character)
        manager['character_displayed'] = True
       
    if len(ROOMS[character['room']['id']]['chest']) != 0:
        if 'Open chest' not in ROOMS[character['room']['id']]['special_options']:
            ROOMS[character['room']['id']]['special_options'].append('Open chest')
            display(ROOMS[character['room']['id']]['special_options'], character)
    
    print()
    print("1 - [Go to another room]")
    print("2 - [Check inventory]")
        
    new_options = print_special_options(special_options)
    print()
    selection = ask_int(1, 2 + new_options)

    if selection == 1:
        return 'Another room'
    elif selection == 2:
        return 'Inventory'
    else:
        selection -= 3
        if special_options[selection] == "Play with cat":
            so.pet_cat(character)

        elif special_options[selection] == "Play piano":
            so.play_piano()
            
        elif special_options[selection] == "Open chest":
            so.open_chest(character)
        
        elif special_options[selection] == "Poster with a knife":
            so.knife_poster(character)
            ROOMS[character['room']['id']]['special_options'].remove(special_options[selection])
        
        elif special_options[selection] == "Get a train toy":
            so.get_toy('train', character)
            ROOMS[character['room']['id']]['special_options'].remove(special_options[selection])
        
        elif special_options[selection] == "Get a plushie":
            so.get_toy('plushie', character)
            ROOMS[character['room']['id']]['special_options'].remove(special_options[selection])
        
        elif special_options[selection] == "Open drawner":
            so.open('drawner', character)
            ROOMS[character['room']['id']]['special_options'].remove(special_options[selection])  
            
        elif special_options[selection] == 'window':
            character['hp'] = 0
        
        manager['character_displayed'] = False
        return 0

# TO-DO:



    # Item add key (index whatever)

# display([["Pet cat"], ["pick your nose"]])
