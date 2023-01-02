import game.item as it

from utils.functions import ask_int, pause


def display(inventory):
    print('----- INVENTORY -----')
    if len(inventory) == 0:
        print("Empty")
    else:
        for item in inventory:
            it.display(item)
    print('-'*21)


def options(inventory):
    mapp = []
    for i, item in enumerate(inventory):
        if not item['type'] == 'key' and item['consumable']:
            duration = item['duration']
            print(f"{len(mapp) + 1} - Use {item['name']} {f'[Duration: {duration}]' if duration > 0 else ''}")
            mapp.append(i)

    if len(mapp) == 0:
        pause()
        return
    else:
        print(f"{len(mapp) + 1} - Do nothing")
        inp = ask_int(1, len(mapp) + 1) - 1
        if inp == len(mapp):
            return
        else:
            return inventory[mapp[inp]]


def use_item(character, item):
    for trait, val in item['traits'].items():
        character[trait] += val
        print(f"{'+' if val > 0 else ''}{val} {trait}")

    if item['duration'] > 0:
        character['ephemeral_items'].append(item)

    if character['hp'] > character['maxhp'] and not item['special']:
        character['hp'] = character['maxhp']

    if item['consumable']:
        delete_item(character, item)


def disable_item(character, item):
    for trait, val in item['traits'].items():
        character[trait] -= val
        print(f"{'+' if (-val) > 0 else ''}{-val} {trait}")


def get_key(inventory, id):
    for item in inventory:
        if item['type'] == 'key' and item['id'] == id:
            return item
    return None


def add_item(character, item):
    character['inventory'].append(item)
    if not item['type'] == 'key' and not item['consumable']:
        use_item(character, item)


def delete_item(character, item):
    character['inventory'].remove(item)
    if not item['type'] == 'key' and not item['consumable']:
        disable_item(character, item)
