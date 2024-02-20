# my ta is cole
def common_values(set_1, set_2):
    return len(set_1.intersection(set_2)) != 0 

assert common_values({1, 2, 3}, {3, 4, 5}) == True
assert common_values({1, 2, 3}, {30, 40, 50}) == False