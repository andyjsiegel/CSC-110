# my TA is cole
def remove_and_append(original_list, to_remove_list, to_append_list):
    for i in range(len(original_list)-1,-1,-1):
        if original_list[i] in to_remove_list:
            original_list.pop(i)
    original_list.extend(to_append_list)
    return original_list

print(remove_and_append([1,2,3], [2,3,4], [10,11]))