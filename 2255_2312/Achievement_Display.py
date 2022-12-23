import Achievement_Manager as am 

TOTAL = 10
# TOTAL must be a constant since like that we work

# This could be modified if the user wants to so we leave them
next_key = "C"
previous_key = "B"
exit_key = "E"

path = "Data.csv"

def paint(count, total, index, name_from_index, description):
    """ Makes the display of the achievement

    Args:
        count (int): total of achievements completed
        total (int): total of achievements available
        index (int): index of the achievement
        name_from_index (String): name of the achievement
        description (String): description of the achievement
    """
    print("----- ACHIEVEMENTS -----")
    print()
    print(f"ACHIEVEMENTS ({count} of {total})")
    print()
    print(f"{index + 1} - {name_from_index}")
    print(f"\t{description}")
    print()
    print(f"{next_key} - Next")
    print(f"{previous_key} - Previous")
    print(f"{exit_key} - Exit")
    result =  input()
    
    if result.upper() == next_key:
        if index < count -1:
            paint_logic(index+1)
        else:
            paint_logic(index)
    elif result.upper() == previous_key:
        if(index > 0):
            paint_logic(index -1)
        else:
            paint_logic(index)
    elif result.upper == exit_key:
        return 1
        
    else:
        pass

      
    
def paint_logic(index_to_paint):
    """Gets the data for the paint method

    Args:
        index_to_paint (int): Index of the achievement you want to display
    """
    data = am.read_achievements(path)
    count = len(data)
    name_from_index = am.separate_achievement(data[index_to_paint])[0]
    description = am.separate_achievement(data[index_to_paint])[1]
    
    paint(count, TOTAL, index_to_paint, name_from_index, description)
    
    
def start_painting():
    paint_logic(0)

