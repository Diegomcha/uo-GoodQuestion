from opts import ITEMS, QUALITIES, SHIRTS_NAMES, PANTS_NAMES, SHOES_NAMES, BASE_DAMAGE_WEAPON
from utils.functions import decide_list, decide_index_rated_list


def generate(available):
    item = {
        'type': decide_list(available),
        'quality': decide_index_rated_list(QUALITIES)
    }
    item['name'] = decide_list(ITEMS[item['type']]['names']) if not QUALITIES[item['quality']]['special'] else decide_list(ITEMS[item['type']]['special_names'])
    item['traits'] = ITEMS[item['type']]['traits'][item['quality']]
    item['consumable'] = ITEMS[item['type']]['consumable']
    print(item['name'])
    item['damage'] = None if item['type'] != 'weapon' else BASE_DAMAGE_WEAPON[item['name']] + int(QUALITIES[item['quality']]['id'])
    
    if item['type'] != 'clothes':
         item['part_of_body'] = None
    else:
        if item['name'] in SHIRTS_NAMES:
            item['part_of_body'] = 'shirt'
        elif item['name'] in PANTS_NAMES:
            item['part_of_body'] = 'pants'
        elif item['name' in SHOES_NAMES]: 
            item['part_of_body'] = 'shoes'
        else: #pijama
            item['part_of_body'] = 'pijama'
        
    
    return item

def generate_key(number):
    item = {
        'type': 'key',
        'number': number
    }
    return item

def display(item):
    print(f"· {item['name']} [{QUALITIES[item['quality']]['name']}]")
    print(f"  {item['type']}{' - CONSUMABLE' if item['consumable'] else ''}")
