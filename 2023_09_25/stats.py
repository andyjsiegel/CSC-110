'''
Andy Siegel
CSC 110
Project 3
This program has several functions which return mean, 
variance, standard deviation, and range
'''
def mean(numbers_list):
    '''
    This function returns the mean of a list of numbers
    Args:
        numbers_list: the list of numbers
    Returns:
        the mean
    '''
    i = 0 # loop variable
    sum = 0
    # make a sum of the numbers in the list
    while i < len(numbers_list):
        sum = sum + numbers_list[i]
        i = i + 1
        
    # try/except clause to catch an empty list
    try:
        return round(sum / len(numbers_list), 2)
    except ZeroDivisionError:
        return 0

def variance(numbers_list):
    '''
    This function returns the variance of a list of numbers
    Args:
        numbers_list: the list of numbers
    Returns:
        the variance
    '''
    average = mean(numbers_list)

    i = 0 # loop variable
    sd_list = [] # standard deviations list

    # get the standard deviation for each value in the list
    while i < len(numbers_list):
        sd_list.append(round(numbers_list[i] - average, 2))
        i = i + 1
    
    i = 0 # loop variable
    squared_deviation_sum = 0
    # squaring each standard deviation in the list and getting the sum of them
    while i < len(numbers_list): 
        sd_list[i] = sd_list[i]**2
        squared_deviation_sum = squared_deviation_sum + sd_list[i]
        i = i + 1

    # variance is the sum of squared deviations 
    variance = round(squared_deviation_sum / (len(sd_list)-1), 2) 
    return variance

def sd(numbers_list):
    '''
    This function returns the standard deviation of a list of numbers
    Args:
        numbers_list: the list of numbers
    Returns:
        the standard deviation
    '''
    # square root of variance (sd) rounded to two decimal places
    return round( variance(numbers_list)**(1/2), 2) 

def list_range(numbers_list):
    '''
    This function returns the range of a list of numbers
    Args:
        numbers_list: the list of numbers
    Returns:
        the range (max - min)
    '''
    # try/except clause in case of an empty list
    try:
        min = numbers_list[0]
        max = numbers_list[0]
    except IndexError:
        min = 0
        max = 0
    
    i = 0 # loop variable
    while i < len(numbers_list):
        if numbers_list[i] <= min:
            min = numbers_list[i]
        
        if numbers_list[i] >= max:
            max = numbers_list[i]

        i = i + 1

    range = max - min
    return range

