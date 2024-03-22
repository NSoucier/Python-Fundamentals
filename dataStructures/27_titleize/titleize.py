def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lst = phrase.split(' ')
    index = 0
    for word in lst:
        lst[index] = word.capitalize()
        index += 1
    return ' '.join(lst)