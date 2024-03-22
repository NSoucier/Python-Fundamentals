def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    snum1 = str(num1)
    snum2 = str(num2)
    
    for num in snum1:
        if snum1.count(num) != snum2.count(num):
            return False
    
    return True


