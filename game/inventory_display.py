

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
    print("Clothes:")
    if character['inventory']['clothes']['pjama'] == None:
        print(f"\tShirt: {character['inventory']['clothes']['shirt']}")
        print(f"\tPants: {character['inventory']['clothes']['pants']}")
        print(f"\tShoes: {character['inventory']['clothes']['feet']}")
    else:
        print(f"\tPijama: {character['inventory']['clothes']['pjama']}")
    #Faith Item
    #If there is no faith item in inventory, won't show
    #(No spoilers)
    if character['inventory']['faith item'] != None:
        print(f"Faith item : {character['inventory']['faith item']}")
    #Weapon
    print(f"Weapon: {character['inventory']['weapon']}")
    
        
