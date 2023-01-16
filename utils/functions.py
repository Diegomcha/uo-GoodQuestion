import random


def ask_options(opts):
    """
    Asks the user to choose from the provided options.

    Parameters
    ----------
    opts : dict[str, str]
        Dictionary with the options using this format:
            {
                'S': 'Select',
                'E': 'Exit'
            }
        Displayed as:
            S - Select
            E - Exit

    Returns
    -------
    str
        Selected key.
    """
    for opt_val, opt_name in opts.items():
        print(f"{opt_val} - {opt_name}")

    selection = ''
    print()
    while not selection in opts.keys():
        selection = input('Selection: ').upper().strip()
    print()

    return selection


def ask_int(start=0, end=0, msg='Selection: '):
    """
    Asks the user for an integer in range [start, end].

    Parameters
    ----------
    start : int
        Opt.
        Start of the range.
    end : int
        Opt.
        End of the range.
    msg : str
        Opt.
        Message to display when asking.

    Returns
    -------
    int
        Integer selected.
    """

    selection = ''
    while not (selection.lstrip('-').isdigit() and start <= int(selection) <= end):
        selection = input(msg).strip()
    print()

    return int(selection)


def print_file(file):
    """
    Prints the contents of the file.

    Parameters
    ----------
    file : str
        Path to the file whose contents to print.
    """

    f = open(file, 'r')
    for line in f:
        print(line, end='')
    f.close()
    print()


def decide(rate):
    """
    Randomly decides whether something should happen according to a probability rate.

    Parameters
    ----------
    rate : float
        The probability in % of that something happening.

    Returns
    -------
    bool
        True if it should happen, false otherwise.
    """
    return random.randint(1, 100) <= rate


def decide_list(list):
    """
    Randomly chooses one element of the list with all items having the same chance.

    Parameters
    ----------
    list : list
        The list of elements to choose from.

    Returns
    -------
    Any
        The chosen item
    """
    return random.choice(list) if not type(list) == type('str') else list


def decide_index_rated_list(list):
    """
    Selects an item from a list of rated elements and returns the index of the selected item.

    Parameters
    ----------
    list : dict[str, Any]
        List of dictionaries with a key called 'rate' containing the rate.

    Returns
    -------
    int
        Index of the selected item.
    """

    total = 0
    for item in list:
        total += item['rate']

    rand = random.randint(1, total)
    last = 0

    for i, item in enumerate(list):
        if last < rand <= (last + item['rate']):
            return i
        else:
            last += item['rate']


def pause(msg=""):
    """
    Pauses the program until the user presses enter.
    """
    input(msg)
    # TODO: If u want we can put here "[ENTER]" or smt like that cause it may be confusing for the user to use
    # TODO: letme know what u think either way having this function is good for readability
