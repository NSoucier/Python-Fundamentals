def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newstr = ''    
    if to_swap.isupper():
        for i in range(0,len(phrase)):
            if phrase[i] == to_swap:
                newstr += phrase[i].lower()
            elif phrase[i] == to_swap.lower():
                newstr += phrase[i].upper()
            else:
                newstr += phrase[i]
    else:
        for i in range(0,len(phrase)):
            if phrase[i] == to_swap.upper():
                newstr += phrase[i].lower()
            elif phrase[i] == to_swap:
                newstr += phrase[i].upper()
            else:
                newstr += phrase[i]
    return newstr