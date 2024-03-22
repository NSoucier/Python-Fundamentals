def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    lower_phrase = phrase.lower()
    vowels = 'aeiou'
    dct = {}
    
    for char in lower_phrase:
        index = vowels.find(char)
        if index != -1:
            if (f"{vowels[index]}" in dct):
                dct[f"{vowels[index]}"] += 1
            else:
                dct[f"{vowels[index]}"] = 1
     
    return dct
