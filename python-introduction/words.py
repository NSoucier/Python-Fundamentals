def print_upper_words(words, must_start_with):
    """For a list of words, print out each word on a separate line, but in all uppercase.
    This also only prints words that start with one the letters listed in the second parameter.
    """
    for word in words:
        for char in must_start_with:
            if word[0] == char:
                print(word.upper())
                break

        

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})