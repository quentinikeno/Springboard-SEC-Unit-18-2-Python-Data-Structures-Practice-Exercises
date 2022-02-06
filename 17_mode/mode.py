def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    highest_count = 0
    mode = None
    nums_set = set(nums)
    
    for num in nums_set:
        count = nums.count(num)
        if count >  highest_count:
            highest_count = count
            mode = num
    
    return mode