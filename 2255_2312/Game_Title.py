import Achievement_Display as AD

def print_title():
    print("""
 e88~~\    ,88~-_     ,88~-_   888~-_           ,88~-_   888   | 888~~  ,d88~~\ ~~~888~~~ 888   ,88~-_   888b    | 
d888      d888   \   d888   \  888   \         d888   \  888   | 888___ 8888       888    888  d888   \  |Y88b   | 
8888 __  88888    | 88888    | 888    |       88888    | 888   | 888    `Y88b      888    888 88888    | | Y88b  | 
8888   | 88888    | 88888    | 888    |       88888    | 888   | 888     `Y88b,    888    888 88888    | |  Y88b | 
Y888   |  Y888   /   Y888   /  888   /         Y888 \ /  Y88   | 888       8888    888    888  Y888   /  |   Y88b| 
 "88__/    `88_-~     `88_-~   888_-~           `88__X    "8__/  888___ \__88P'    888    888   `88_-~   |    Y888  
 
 --------------------------------------------------------------------------------------------------------------------
                1- New game
                2- Achievements
                3- Credits
                █- Exit""")
    
    print()
    return input("\t\t")
    
    

def title_logic():
    answer  = print_title()
    
    if answer == "1":
        pass
    elif answer == "2":
        AD.start_painting()
        title_logic()
    elif answer == "3":
        read_credits()
        title_logic()
    else:
        pass

def read_credits():
    print(" --------------------------------------------------------------------------------------------------------------------")
    for line in open("Credits.csv", "r").readlines():
        print(line)
    input()
    
title_logic()
