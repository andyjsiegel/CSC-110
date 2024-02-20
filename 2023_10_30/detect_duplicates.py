# Programming Problem 22
def has_duplicate(list):
    return not len(list) == len(set(list))

print( has_duplicate([]) ) # False
print( has_duplicate([1, 2, 3, 1]) ) # True
print( has_duplicate([1, "a", "b", 4, 5]) ) # False
print( has_duplicate([1, "a", "a", 2, 3, 4]) ) # True