import game.room as rm
import game.inventory_display as inv

from utils.functions import ask_int


# special_options = [option1.....]
def print_special_options(special_options):
    for i, element in enumerate(special_options):
        print(f"{i+3} - {element}")
    return len(special_options)


def display(special_options, character):
    print(f"""----- OPTIONS -----

1 - Go to another room
2 - Check inventory""")
    new_options = print_special_options(special_options)
    print()
    selection = ask_int(1, 2 + new_options)

    if selection == 1:
        rm.move(character, character['room'])
        display(special_options, character)
    elif selection == 2:
        inv.display_inventory(character)
        input()
    else:
        selection -= 3
        if special_options[selection] == "Pet cat":
            pet_cat()

        elif special_options[selection] == "Play piano":
            play_piano()


# TO-DO:
def pet_cat():
    print("Miau")


def play_piano():
    print("A piece fell down revealing a key")
    # Item add key (index whatever)

# display([["Pet cat"], ["pick your nose"]])
