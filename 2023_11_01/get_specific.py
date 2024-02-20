def get_elements(dictionary, n):
    the_list = []
    for key, value in dictionary.items():
        if key[0] == key[0].upper():
            the_list.append(value)
        elif key[-1] == key[-1].upper():
            the_list.append(value)
        elif value >= n:
            the_list.append(value)

    return the_list
data = {'Alpha':10, 'bravo':25, 'charliE':15, 'dELTa':2}
print( get_elements(data, 12) ) # [10, 25, 15]