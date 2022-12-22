
def is_in_file(path, name):
    """Scans through the the file if possible, and returns wether the achievment is in the file or not

    Args:
        path (dir): Directory of the file you want to read through
        name (string): The name of the achivement to check

    Returns:
        True : if in file
        False : if not in file
        -1 : ERROR_WRONG_PATH
    """
    try:
        read_file = open(path, "r")
        data = read_file.readlines()
        
        for line in data:
            if line.count(name) != 0:
                return True
            
        read_file.close()
        return False
    except:
        return -1
    
def write_achivement(path, name, description):
    """ Checks if the given achivement is in the file, and in case it is not, it writes
    
        Args:
        path (dir): Directory of the file you want to modify
        name (string): The name of the achivement to check
        description (string): The description of the achivement

    Returns:
        1 : if already in file
        0 : if written propperly
        -1 : ERROR_WRONG_PATH
        """
    if is_in_file(path, name) == True:
        return 1
    elif is_in_file(path,name) == False:
        write_file = open(path, "a")
        write_file.write(name + "-"+description+"\n")
        write_file.close()
        return 0
    else:
        return -1

def read_achievments(path):
    """Returns all the values stored in the file 

    Args:
        path (dir): Directory of the file you want to read through

    Returns:
        data : list of the values stored in the file
        -1 : ERROR_WRONG_PATH
    """
    try:
        file = open(path, "r")
        data = file.readlines()
        return data
    except:
        return -1
    
# Achivements will be saved in a list like so:
# achivements = [[a1, d1], [a2,d2], [a3,d3], [a4,d4]...]