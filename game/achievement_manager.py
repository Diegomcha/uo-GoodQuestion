def check_file(path):
    """Checks whether data.txt exists or not

    Parameters
    ----------
    path : str
        Path where data.txt should be

    Returns
    -------
    bool
        True if the file exists, else False
    """
    try:
        f = open(path, 'r')
        f.close()
        return True
    except:
        return False


def is_in_file(path, name):
    """Scans through the the file if possible, and returns wether the achievment is in the file or not

    Parameters
    ----------
        path : str
            Directory of the file you want to read through
        name : str 
            The name of the achivement to check

    Returns
    -------
    bool / int:
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


def write_achievement(path, id):
    """ Checks if the given achivement is in the file, and in case it is not, it writes

    Parameters
    ----------
    path : str
        Directory of the file you want to modify
    name : str
        The name of the achivement to check
    description : str
        The description of the achivement

    Returns
    -------
    int:
        1 : if already in file
        0 : if written propperly
    """
    if is_in_file(path, id[0]) == True:
        return 1
    else:
        write_file = open(path, "a")
        write_file.write(id[0] + ": "+id[1] + "\n")
        write_file.close()
        return 0


def read_achievements(path):
    """Returns all the values stored in the file 

    Parameters
    ----------
    path : str
        Directory of the file you want to read through

    Returns
    -------
    list / int:
        List of the values stored in the file or -1 if ERROR_WRONG_PATH
    """
    try:
        file = open(path, "r")
        data = file.readlines()
        file.close()
        return data
    except:
        return -1


def separate_achievement(achievement_string):
    """Separates the string into two parts, the name and the description

    Parameters
    ----------
    achievement_string : str
        The string to separate

    Returns
    -------
    list:
        List [name, description]
    """
    result = achievement_string.split(":")
    return result
