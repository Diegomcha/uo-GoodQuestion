from opts import ITEMS, QUALITIES, SHIRTS_NAMES, PANTS_NAMES, SHOES_NAMES
from utils.functions import decide_list, decide_index_rated_list


def generate(available):
    item = {
        'type': decide_list(available),
        'quality': decide_index_rated_list(QUALITIES)
    }
    item['name'] = decide_list(ITEMS[item['type']]['names']) if QUALITIES[item['quality']]['special'] != True else decide_list(ITEMS[item['type']]['special_names'])
    item['traits'] = ITEMS[item['type']]['traits'][item['quality']]
    item['consumable'] = ITEMS[item['type']]['consumable']
    
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


def display(item):
    print(f"· {item['name']} [{QUALITIES[item['quality']]['name']}]")
    print(f"  {item['type']}{' - CONSUMABLE' if item['consumable'] else ''}")
