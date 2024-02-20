# ta is cole
def my_max(array):
        if len(array) <= 0 or array[0] == None: return None
        maximum = array[0]
        for number in array:
            if number > maximum:
                maximum = number
        return maximum

def nested_max(main_array):
    maxes_of_arrays = []
    for array in main_array:
            maxes_of_arrays.append(my_max(array))
    return my_max(maxes_of_arrays)

print(nested_max([[1, 2, 3, 2, 1],
                     [2, 3, 2, 1, 5],
                     [0, 1]]))
print(nested_max([[], []]))