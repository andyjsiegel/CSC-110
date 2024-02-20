def all_mappings(dict):
    the_list = []
    for key in dict.keys():
        for item in dict[key]:
            the_list.append(tuple([key, item]))
    return the_list

print( all_mappings({"a": [7, 3, 1]}) ) # [("a", 7), ("a", 3), ("a", 1)]
print( all_mappings({"a": [8], "b": [2]}) ) # [("a", 8), ("b", 2)]
print( all_mappings({"a": [], "b": [2]}) ) # [("b", 2)]
print( all_mappings({}) ) # []