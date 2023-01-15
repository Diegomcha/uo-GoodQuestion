from opts import QUALITIES
from utils.functions import ask_int
import game.item as it


def display_inventory(character):
    print('\t\t----- INVENTORY -----')
    print()
    # Keys
    print(f"\t\t - Keys: {'None' if len(character['inventory']['keys']) == 0 else len(character['inventory']['keys'])}")
    #print(f" - Medicies: {'None' if len(character['inventory']['medicines']) == 0 else element['name'] for element in character['inventory']['medicine']}")

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

    # for element in character['inventory']['medicine']:
    #     print(f"\t- {element}")
    # Items
    #print(f" - Items: {'None' if len(character['inventory']['items']) == 0 else ''}")
    # for element in character['inventory']['items']:
    #    print(f"     · {element['name']}")
    # Clothes
    print("\t\t - Clothes:")
    if character['inventory']['clothes']['pijama'] == None:
        print(f"\t\t    · Shirt: {character['inventory']['clothes']['shirt']['name'] if character['inventory']['clothes']['shirt'] != None else None}")
        print(f"\t\t    · Pants: {character['inventory']['clothes']['pants']['name'] if character['inventory']['clothes']['pants'] != None else None}")
        print(f"\t\t    · Shoes: {character['inventory']['clothes']['shoes']['name'] if character['inventory']['clothes']['shoes'] != None else None}")
    else:
        print(f"\t\t    · Pijama: {character['inventory']['clothes']['pijama']['name']}")
        print(f"\t\t    · Shoes: {character['inventory']['clothes']['shoes']['name'] if character['inventory']['clothes']['shoes'] != None else None}")

    # Faith Item
    # If there is no faith item in inventory, won't show
    # (No spoilers)
    if character['inventory']['faith_item'] != None:
        print(f"\t\t - Faith item: {character['inventory']['faith_item']['name']} [{character['inventory']['faith_item']['traits']['shield']}]")
    # Weapon
    print(f"\t\t - Weapon: {character['inventory']['weapon']['name'] if not character['inventory']['weapon'] == None else None} {'['+str(character['inventory']['weapon']['damage']) + ']' if not character['inventory']['weapon'] ==  None else '' }")

    print()
    ask_use_items(character)


def ask_use_items(character):
    if len(character['inventory']['medicine']) > 0 or len(character['inventory']['energetic_drinks']) > 0:
        if len(character['inventory']['medicine']) > 0:
            for i, medicine in enumerate(character['inventory']['medicine']):
                print(f"{i+1} - [Use {medicine['name']}] [{medicine['traits']['hp']}hp]")

        if len(character['inventory']['energetic_drinks']) > 0:
            for j, drink in enumerate(character['inventory']['energetic_drinks']):
                print(f"{i+j+1} - [Use {drink['name']}] [{drink['traits']['swiftness']}sp]")

        print(f"{len(character['inventory']['medicine']) + len(character['inventory']['energetic_drinks']) + 1} - [Leave]")
        print()
        result = ask_int(1, len(character['inventory']['medicine']) + len(character['inventory']['energetic_drinks']) + 1)
        if result == len(character['inventory']['medicine']) + len(character['inventory']['energetic_drinks']) + 1:
            return 0
        else:
            it.consume_item(character['inventory']['medicine'][result - 1], character)

    else:
        print(f"1 - [Leave]")
        print()
        if ask_int(1, 1) == 1:
            return 0
