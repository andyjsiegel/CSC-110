def mutate_dict(dict_1, set):
    for value in set:
        if value not in dict_1:
            dict_1[value] = 0
    return dict_1

test_dictionary = {"z": 1, "x": 2, "r": 20}
mutate_dict(test_dictionary, {"a", "z", "r", "b"} )
assert test_dictionary == {"z": 1, "x": 2, "r": 20, "a": 0, "b": 0}