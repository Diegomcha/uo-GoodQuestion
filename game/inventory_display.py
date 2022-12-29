

def display_inventory(character):
    print('----INVENTORY----')
    print()
    #Keys
    print(f"Keys : {len(character['inventory']['keys'])}")
    print("Medicine:")
    for element in character['inventory']['medicine']:
        print(f"\t- {element}")
    #Items
    print("Items:")
    for element in character['inventory']['items']:
        print(f"\t- {element}")
    #Clothes
    if character['inventory']['clothes']['pjama'] == None:
        print(f"Shirt: {['inventory']['clothes']['shirt']}")
        print(f"Pants: {['inventory']['clothes']['pants']}")
        print(f"Shoes: {['inventory']['clothes']['feet']}")
    else:
        print(f"Pijama: {['inventory']['clothes']['pjama']}")
    #Faith Item
    #If there is no faith item in inventory, won't show
    #(No spoilers)
    if ['inventory']['faith item'] != None:
        print(f"Faith item : {['inventory']['faith item']}")
    #Weapon
    print(['inventory']['weapon'])
    
        