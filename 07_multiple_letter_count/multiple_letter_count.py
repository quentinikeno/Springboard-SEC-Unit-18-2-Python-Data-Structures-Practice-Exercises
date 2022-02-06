def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    lower_phrase = phrase.lower()
    letter_dict = {}
    letters_set = set(lower_phrase)
    for letter in letters_set:
        letter_dict[letter] = lower_phrase.count(letter)
    return letter_dict