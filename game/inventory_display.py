from opts import QUALITIES
from utils.functions import ask_int
import game.item as it

def display_inventory(character):
    print('\t\t----- INVENTORY -----')
    print()
    # Keys
    print(f"\t\t - Keys: {'None' if len(character['inventory']['keys']) == 0 else len(character['inventory']['keys'])}")
    #print(f" - Medicies: {'None' if len(character['inventory']['medicines']) == 0 else element['name'] for element in character['inventory']['medicine']}")
    
    print("\t\t - Medicines:", end = " ")
    if len(character['inventory']['medicine']) == 0:
        print("None")
        
    else:
        printed = []
        for element in character['inventory']['medicine']:
            if element not in printed:
                printed.append(element)
                count = character['inventory']['medicine'].count(element)
                if  count == 1:
                    if element == character['inventory']['medicine'][0]:
                        print(f"{element['name']}[{QUALITIES[element['quality']]['name']}]", end = " ")
                    else:
                        print(f", {element['name']}[{QUALITIES[element['quality']]['name']}]", end = " ")
                else:
                    if element == character['inventory']['medicine'][0]:
                        print(f"{element['name']}[{QUALITIES[element['quality']]['name']}] X{count}", end = " ")
                    else:
                        print(f", {element['name']}[{QUALITIES[element['quality']]['name']}] X{count}", end = " ")
        print()
        
    # for element in character['inventory']['medicine']:
    #     print(f"\t- {element}")
    # Items
    #print(f" - Items: {'None' if len(character['inventory']['items']) == 0 else ''}")
    #for element in character['inventory']['items']:
    #    print(f"     · {element['name']}")
    # Clothes
    print("\t\t - Clothes:")
    if character['inventory']['clothes']['pijama'] == None:
        print(f"\t\t    · Shirt: {character['inventory']['clothes']['shirt']}")
        print(f"\t\t    · Pants: {character['inventory']['clothes']['pants']}")
        print(f"\t\t    · Shoes: {character['inventory']['clothes']['shoes']}")
    else:
        print(f"\t    · Pijama: {character['inventory']['clothes']['pijama']}")
    # Faith Item
    # If there is no faith item in inventory, won't show
    # (No spoilers)
    if character['inventory']['faith_item'] != None:
        print(f"\t\t - Faith item: {character['inventory']['faith_item']}")
    # Weapon
    print(f"\t\t - Weapon: {character['inventory']['weapon']['name'] if not character['inventory']['weapon'] == None else None} {'['+str(character['inventory']['weapon']['damage']) + ']' if not character['inventory']['weapon'] ==  None else '' }")

    print()
    ask_use_items(character)
    
def ask_use_items(character):
    if len(character['inventory']['medicine']) > 0:
        for i,medicine in enumerate(character['inventory']['medicine']):
            print(f"·{i+1}- [Use {medicine['name']}] [{medicine['traits']['heal']}hp]")
        
        print(f"·{i+2}- [Leave]")
        
        result = ask_int(1, i+2)
        print(i+2)
        if result == i+2:
            return 0
        else:
            it.consume_item(character['inventory']['medicine'][result -1],character)
    
    else:
        print(f"·1- [Leave]")
        if ask_int(1,1) == 1:
            return 0