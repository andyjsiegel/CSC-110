def combine(first_list, second_list):
    for item in second_list:
        first_list.append(item)
        
    return first_list

test_list = []
combine(test_list, []) 
print(test_list) # []

test_list = [1, 2, 3]
combine(test_list, [1, 1]) 
print(test_list) # [1, 2, 3, 1, 1]

test_list = [1, 2, 3, 1, 5]
combine(test_list, [])
print(test_list) # [1, 2, 3, 1, 5]