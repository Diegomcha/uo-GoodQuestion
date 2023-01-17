from opts import QUALITIES, ROOMS
from utils.functions import ask_int, pause
import game.item as it


def display_inventory(character):
    """Method that displays the inventory of the character and gives the option of using items 
    if they are in the inventory

    Parameters
    ----------
    character : dict[str, Any]
        dictionary storing all the attributes of the character
    """
    print('\t\t----- INVENTORY -----')
    print()
    # Keys
    if len(character['inventory']['keys']) != 0:
        print(f"\t\t - Keys: ")
        for key in character['inventory']['keys']:
            if len(character['locked_doors_visited']) == 0 or key['number'] not in character['locked_doors_visited']:
                print("\t\t\t[?????]")
            else:
                print(f"\t\t\t[{ROOMS[key['number']]['resemblance'].upper()}]")
    else:
        print(f"\t\t - Keys: None")
    # print(f" - Medicies: {'None' if len(character['inventory']['medicines']) == 0 else element['name'] for element in character['inventory']['medicine']}")

    print("\t\t - Medicines:", end=" ")
    if len(character['inventory']['medicine']) == 0:
        print("None")

    else:
        printed = []
        for element in character['inventory']['medicine']:
            if element not in printed:
                printed.append(element)
                count = character['inventory']['medicine'].count(element)
                if count == 1:
                    if element == character['inventory']['medicine'][0]:
                        print(f"{element['name']}[{QUALITIES[element['quality']]['name']}]", end=" ")
                    else:
                        print(f", {element['name']}[{QUALITIES[element['quality']]['name']}]", end=" ")
                else:
                    if element == character['inventory']['medicine'][0]:
                        print(f"{element['name']}[{QUALITIES[element['quality']]['name']}] X{count}", end=" ")
                    else:
                        print(f", {element['name']}[{QUALITIES[element['quality']]['name']}] X{count}", end=" ")
        print()

    print("\t\t - Energetic Drinks:", end=" ")
    if len(character['inventory']['energetic_drinks']) == 0:
        print("None")

    else:
        printed = []
        for element in character['inventory']['energetic_drinks']:
            if element not in printed:
                printed.append(element)
                count = character['inventory']['energetic_drinks'].count(element)
                if count == 1:
                    if element == character['inventory']['energetic_drinks'][0]:
                        print(f"{element['name']}[{QUALITIES[element['quality']]['name']}]", end=" ")
                    else:
                        print(f", {element['name']}[{QUALITIES[element['quality']]['name']}]", end=" ")
                else:
                    if element == character['inventory']['energetic_drinks'][0]:
                        print(f"{element['name']}[{QUALITIES[element['quality']]['name']}] X{count}", end=" ")
                    else:
                        print(f", {element['name']}[{QUALITIES[element['quality']]['name']}] X{count}", end=" ")
        print()

    # Clothes
    print("\t\t - Clothes:")
    if character['inventory']['clothes']['pijama'] == None:
        if character['inventory']['clothes']['shirt']:
            print(f"\t\t    · Shirt: {character['inventory']['clothes']['shirt']['name']} [+{character['inventory']['clothes']['shirt']['traits']['sneak']} sneak]")
        else:
            print("\t\t    · Shirt: None")

        if character['inventory']['clothes']['pants']:
            print(f"\t\t    · Pants: {character['inventory']['clothes']['pants']['name']} [+{character['inventory']['clothes']['pants']['traits']['sneak']} sneak]")
        else:
            print("\t\t    · Pants: None")

    else:
        print(f"\t\t    · Pijama: {character['inventory']['clothes']['pijama']['name']} [+{character['inventory']['clothes']['pijama']['traits']['sneak']} sneak]")

    if character['inventory']['clothes']['shoes']:
        print(f"\t\t    · Shoes: {character['inventory']['clothes']['shoes']['name']} [+{character['inventory']['clothes']['shoes']['traits']['sneak']} sneak]")
    else:
        print("\t\t    · Shoes: None")

    # Faith Item
    # If there is no faith item in inventory, won't show
    # (No spoilers)
    if character['inventory']['faith_item'] != None:
        print(f"\t\t - Faith item: {character['inventory']['faith_item']['name']} [+{character['inventory']['faith_item']['traits']['shield']} shield]")
    # Weapon
    if character['inventory']['weapon'] != None:
        print(f"\t\t - Weapon: {character['inventory']['weapon']['name']} [+{character['inventory']['weapon']['traits']['strength']} damage]")
    else:
        print("\t\t - Weapon: None")

    print()
    ask_use_items(character)


def ask_use_items(character):
    """Method that asks if the player really want to use the item

    Parameters
    ----------
    character : dict[str, Any]
        dictionary storing all the attributes of the character
    """
    if len(character['inventory']['medicine']) > 0 or len(character['inventory']['energetic_drinks']) > 0:
        if len(character['inventory']['medicine']) > 0:
            for i, medicine in enumerate(character['inventory']['medicine']):
                print(f"{i+1} - [Use {medicine['name']}] [+{medicine['traits']['hp']} hp]")
            i += 1
        else:
            i = 0

        if len(character['inventory']['energetic_drinks']) > 0:
            for j, drink in enumerate(character['inventory']['energetic_drinks']):
                print(f"{i+j+1} - [Use {drink['name']}] [+{drink['traits']['swiftness']} swiftness]")
        else:
            j = 0

        print(f"{len(character['inventory']['medicine']) + len(character['inventory']['energetic_drinks']) + 1} - [Leave]")
        print()
        result = ask_int(1, len(character['inventory']['medicine']) + len(character['inventory']['energetic_drinks']) + 1)
        result -= 1
        if result == len(character['inventory']['medicine']) + len(character['inventory']['energetic_drinks']):
            return 0
        elif result < i:
            it.consume_item(character['inventory']['medicine'][result], character)
        else:
            it.consume_item(character['inventory']['energetic_drinks'][result-i], character)

    else:
        pause()
