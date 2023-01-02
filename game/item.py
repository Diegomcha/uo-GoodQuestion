from opts import ITEMS, QUALITIES
from utils.functions import decide_list, decide_index_rated_list


def generate(available):
    item = {
        'type': decide_list(available) if type(available[0]) is str else available[decide_index_rated_list(available)]['type'],
        'quality': decide_index_rated_list(QUALITIES)
    }
    item['special'] = QUALITIES[item['quality']]['special']
    item['name'] = decide_list(ITEMS[item['type']]['special_names']) if item['special'] else decide_list(ITEMS[item['type']]['names'])
    item['traits'] = ITEMS[item['type']]['traits'][item['quality']]
    item['consumable'] = ITEMS[item['type']]['consumable']
    item['duration'] = ITEMS[item['type']]['duration']
    return item


def display(item):
    if item['type'] == 'key':
        print(f" · {item['name']} [KEY]")
    else:
        print(f" · {item['name']} [{QUALITIES[item['quality']]['name']}{' | CONSUMABLE' if item['consumable'] else ''}]")
        for key in item['traits'].keys():
            value = item['traits'][key]
            print(f"   {'+' if value > 0 else ''}{value} {key}")
