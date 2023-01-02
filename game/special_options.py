import game.item as it
import random

from opts import ROOMS, PREFABS
from game.game_manager import manager
from utils.functions import ask_int

def pet_cat(character):
    manager['times_cat_pet'] += 1
    
    print("Cat meows")
    
    if manager['times_cat_pet'] == 4:
        print("Cat comes a little bit closer")
            
    elif manager['times_cat_pet'] == 7:
        print("Cat starts to purr")
        
    elif manager['times_cat_pet'] == 10:
        it.pick_items(PREFABS['cat_item'], 1, character)
    
    print()

def play_piano():
    print("A piece fell down revealing a key")
    
def open_chest(character):
    print("The chest contains:")
    
    for i, item in enumerate(ROOMS[character['room']['id']]['chest']):
        if item['type'] == 'weapon':
            print(f"\t{i +1}- Name: {item['name']}, Quality: {item['quality']}, Damage: {item['damage']}")
        else:
            print(f"\t{i +1}- Name: {item['name']}, Quality: {item['quality']}, Traits: {item['traits']}")
    print(f"\t{i+2}- [Back]")
    print()
    
    result = ask_int(1, i+2)
    
    if result != i+2:
        win = ROOMS[character['room']['id']]['chest'][result-1]
        ROOMS[character['room']['id']]['chest'].remove(win)
        
        it.pick_items(win,1, character)
    pass

def knife_poster(character):
    print('...', end = "")
    input()
    print('You find a poster with the image of your friends and a knife stabbed to it')
    input()
    print('\t1- [Grab knife]\n\t2- [Leave]')
    print()
    
    if ask_int(1,2) == 1:
        it.pick_items(PREFABS['kitchen_knife'], 1, character)
        ROOMS[character['room']['id']]['special_options'].remove("Poster with a knife")
        
    
def get_toy(type, character):
    if type == 'train':
        print('You grab the train', end="")
        input()
        if(random.random() > 0.5):
            print("A wheel fell off", end = "")
        else:
            print("A rat scared you and the train fell on your feet", end="")
            input()
            print('You took 5 damage', end= " ")
            character['hp'] -= 5
        input()
            
    if type == 'plushie':
        print('You squish the plushie and it makes some scary noise', end= "")
        input()
        print('You put it down', end = "")
        input()
            
def open(type, character):
    loot = None if random.random() > 0.2 else it.generate(["medicine", "faith_item"])
    print(f'You opened a {type}', end = "")
    input()
    if loot == None:
        print("You found nothing inside", end = "")
    else:
        print(f"You have found an {loot['name']}", end= "")
        it.pick_items(loot, 1, character)
    input()
    
    
    
