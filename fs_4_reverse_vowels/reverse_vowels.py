from re import I


def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    final_string_list = []
    
    only_vowels_reversed = [char for char in s if char.lower() in 'aeiou']
    only_vowels_reversed.reverse()
    
    vowel_count = 0
   
    for i in range(len(s)):
        if s[i].lower() in 'aeiou':  
            final_string_list.append(only_vowels_reversed[vowel_count])
            vowel_count += 1
        else:
            final_string_list.append(s[i])
            
    return "".join(final_string_list)