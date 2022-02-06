def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    frequency_dict_num1 = {}
    frequency_dict_num2 = {}
    num1_str = str(num1)
    num2_str = str(num2)
    
    num1_digits = {digit for digit in num1_str}
    num2_digits = {digit for digit in num2_str}
    
    for digit in num1_digits:
        frequency_dict_num1[digit] = num1_str.count(digit)
    for digit in num2_digits:
        frequency_dict_num2[digit] = num2_str.count(digit)
        
    return frequency_dict_num1 == frequency_dict_num2