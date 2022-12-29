def display_inventory(character):
    print('----- INVENTORY -----')
    print()
    # Keys
    print(f" - Keys: {'None' if len(character['inventory']['keys']) == 0 else character['inventory']['keys'].join(', ') }")
    print(f" - Medicines: {'None' if len(character['inventory']['medicine']) == 0 else character['inventory']['medicine'].join(', ') }")
    # for element in character['inventory']['medicine']:
    #     print(f"\t- {element}")
    # Items
    print(f" - Items: {'None' if len(character['inventory']['items']) == 0 else ''}")
    for element in character['inventory']['items']:
        print(f"     · {element['name']}")
    # Clothes
    print(" - Clothes:")
    if character['inventory']['clothes']['pijama'] == None:
        print(f"    · Shirt: {character['inventory']['clothes']['shirt']}")
        print(f"    · Pants: {character['inventory']['clothes']['pants']}")
        print(f"    · Shoes: {character['inventory']['clothes']['feet']}")
    else:
        print(f"    · Pijama: {character['inventory']['clothes']['pijama']}")
    # Faith Item
    # If there is no faith item in inventory, won't show
    # (No spoilers)
    if character['inventory']['faith_item'] != None:
        print(f" - Faith item: {character['inventory']['faith item']}")
    # Weapon
    print(f" - Weapon: {character['inventory']['weapon']}")
