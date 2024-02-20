def find_minimum_index(list, index):
    minimum_index = index
    for idx in range(index, len(list)):
        if list[idx] < list[minimum_index]:
            minimum_index = idx
    return minimum_index

def selection_sort(the_list):
    for index in range(len(the_list)):
        min_index = find_minimum_index(the_list, index)
        the_list[index], the_list[min_index] = the_list[min_index], the_list[index]

    return the_list

test_list = [5, 10, 20, 6, 7, 9, 15, 10, 12]
selection_sort(test_list)
print(test_list)