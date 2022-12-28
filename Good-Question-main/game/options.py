from game.room import move
from utils.functions import ask_int


#special_options = [option1.....]
def print_special_options(special_options):
    counter = 3
    for element in special_options:
        print(f"\t{counter} - {element}")
        counter += 1
    return counter - 3
        
        

def display(special_options = [], character = 0):
    print()
    print(f""" 
        ----- OPTIONS----
        1 - Go to another room
        2 - Check Inventory""")
    new_options = print_special_options(special_options)
    selection = ask_int(1, 2 + new_options)
    
    if selection == 1:
        move(character, character['room'])

    elif selection == 2:
        #Display iventory
        print()
    else:
        selection -= 3
        if special_options[selection] == "Pet cat":
            pet_cat()
            
        elif special_options[selection] == "Play piano":
            play_piano()
            
#TO-DO:
def pet_cat():
    print("Miau")
    
def play_piano():
    print("A piece fell down revealing a key")
    #Item add key (index whatever)
        
#display([["Pet cat"], ["pick your nose"]])