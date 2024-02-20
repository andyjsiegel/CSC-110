def csv_to_list(file_name):
    '''
    This function converts a CSV file into a list of items. 
    Args: 
        filename: the name of the CSV file to be converted 
    Returns: 
        a list of items from the CSV file
    '''
    f = open(file_name, 'r')
    csv_as_list = []
    for line in f.readlines():
        for item in line.strip().split(','):
            if item.isnumeric() or "." in item:
                csv_as_list.append(item)

    return csv_as_list

def count_start_digits(numbers):
    '''
    This function counts the number of times each digit from 1 to 9 appears as the first digit in a list of numbers. 
    Args: 
        numbers: a list of numbers 
    Returns: 
        a dictionary with the count of each digit as the first digit in the numbers list
    '''
    start_digits_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for num in numbers:
        if num[0] == '0':
            pass
        else:
            start_digits_dict[int(num[0])] += 1

    return start_digits_dict

def digit_percentages(dictionary):
    '''
    This function calculates the percentage of each digit in a given dictionary. 
    Args: 
        dictionary: a dictionary containing integer values 
    Returns: 
        a dictionary with the percentage of each digit from 1 to 9 in the given dictionary
    '''
    sum = 0
    digit_percents = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for value in dictionary.values():
        sum += value
    print(sum)
    
    i = 1
    for val in dictionary.values():
        percentage = round((val / sum)*100,2) 
        digit_percents[i] = percentage
        i += 1

    return digit_percents

def check_benfords_law(percentages):
    '''
    This function checks if the given percentages follow Benford’s Law. 
    Args: 
        percentages: a dictionary of percentages to be checked 
    Returns: 
        True if the percentages follow Benford’s Law, False otherwise.
    '''
    benfords_values = [30, 17, 12, 9, 7, 6, 5, 5, 4]
    print(percentages)
    i = 0
    for value in percentages.values():
        # print(value)
        if value >= benfords_values[i] - 5 and value <= benfords_values[i]+10:
            pass
        else:
            return False
        i += 1
    
    return True




