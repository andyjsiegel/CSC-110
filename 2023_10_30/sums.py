# Programming Problem 23
def sum_nums(list, integer):
    sum = 0
    for sub_list in list:
        for item in sub_list:
            if item < integer:
                sum += item

    return sum

print( sum_nums([[2, 12, 2], [12, 5, 100, 9]], 10) ) # 18
print( sum_nums([[2, 12, 2], [10, 5, 10, 9]], 10) ) # 18
print( sum_nums([[2, 12, 2], [10, 5, 10, 9]], 0) ) # 0
print( sum_nums([], 10) ) # 0