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
    while not selection in opts.keys():
        selection = input('Selection: ').upper().strip()

    return selection


def ask_int(start, end, msg):
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

    start = start if start else float('-inf')
    end = end if end else float('inf')
    msg = msg if msg else ''

    selection = ''
    while not (selection.lstrip('-').isdigit() and start <= int(selection) <= end):
        selection = input(msg).strip()
    return int(selection)
