def create_list(items, n):
    new_list = [ ]
    for value in items:
        for i in range(n):
            new_list.append(value)
    return new_list

# def create_list(set, integer):
#     set_as_list = []
#     for item in set:
#         for i in range(integer):
#             set_as_list.append(item)
    
#     return set_as_list

items = {"banana", "apple", "pear"}
print( create_list(items, 2))
assert create_list(items, 2) == ['banana', 'banana', 'apple', 'apple', 'pear', 'pear']