def zip_lists(list_1, list_2, list_3):
    the_list = []
    for i in range(len(list_1)):
        the_list.append(tuple([list_1[i], list_2[i], list_3[i]]))

    return the_list

print( zip_lists([1, 2], ["a", "b"], [1.0, 2.0]) ) # [(1, "a", 1.0), (2, "b", 2.0)]
print(zip_lists([], [], []) ) # []
print(list(zip([1, 2], ["a", "b"], [1.0, 2.0])))
print(list(zip([], [], [])))