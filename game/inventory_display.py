def display_inventory(character):
    print('----- INVENTORY -----')
    print()
    # Keys
    print(f" - Keys: {'None' if len(character['inventory']['keys']) == 0 else len(character['inventory']['keys'])}")
    #print(f" - Medicies: {'None' if len(character['inventory']['medicines']) == 0 else element['name'] for element in character['inventory']['medicine']}")
    
    print("  - Medicines:", end = " ")
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
    print(" - Clothes:")
    if character['inventory']['clothes']['pijama'] == None:
        print(f"    · Shirt: {character['inventory']['clothes']['shirt']}")
        print(f"    · Pants: {character['inventory']['clothes']['pants']}")
        print(f"    · Shoes: {character['inventory']['clothes']['shoes']}")
    else:
        print(f"    · Pijama: {character['inventory']['clothes']['pijama']}")
    # Faith Item
    # If there is no faith item in inventory, won't show
    # (No spoilers)
    if character['inventory']['faith_item'] != None:
        print(f" - Faith item: {character['inventory']['faith_item']}")
    # Weapon
    print(f" - Weapon: {character['inventory']['weapon']}")
