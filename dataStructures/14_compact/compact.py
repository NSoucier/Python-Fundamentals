def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    newlst = []

    for i in range(0, len(lst)):
        if lst[i]:
            newlst.append(lst[i])
    return newlst
