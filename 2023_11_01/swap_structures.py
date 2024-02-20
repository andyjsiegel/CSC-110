# Programming Problem 25
def swap(the_dictionary, the_set):
    keys_in_set = []
    for key, value in the_dictionary.items():
        if key in the_set:
            keys_in_set.append(key)
    
    for key in keys_in_set:
        value = the_dictionary[key]
        the_dictionary[value] = key
        del the_dictionary[key]


        

dict_data = {'a':'b', 'c':'d', 'e':'f'}
set_data = {'c', 'e'}
swap(dict_data, set_data)
print(dict_data) # {'a': 'b', 'd': 'c', 'f': 'e'}

dict_data = {23:24, 110:120, 50:45, 70:50, 57:1}
set_data = {23, 110, 57}
swap(dict_data, set_data)
print(dict_data) # {50: 45, 70: 50, 24: 23, 120: 110, 1: 57}

dict_data = {23:24, 110:120, 50:45, 70:50, 57:1}
set_data = {100}
swap(dict_data, set_data)
print(dict_data) # {23:24, 110:120, 50:45, 70:50, 57:1}