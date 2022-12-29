from opts import ITEMS, QUALITIES
from utils.functions import decide_list, decide_index_rated_list


def generate(available):
    item = {
        'type': decide_list(available),
        'quality': decide_index_rated_list(QUALITIES)
    }
    item['name'] = decide_list(ITEMS[item['type']]['names']) if QUALITIES[item['quality']]['special'] != True else decide_list(ITEMS[item['type']['special_names']])
    item['traits'] = ITEMS[item['type']]['traits'][item['quality']]
    item['consumable'] = ITEMS[item['type']]['consumable']
    return item


def display(item):
    print(f"· {item['name']} [{QUALITIES[item['quality']]['name']}]")
    print(f"  {item['type']}{' - CONSUMABLE' if item['consumable'] else ''}")
