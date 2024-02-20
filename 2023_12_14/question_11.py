def remove_vowel_ending(list):
    for i in range(len(list)-1,-1,-1):
        if list[i][-1] in "aeiouAEIOU":
            list.pop(i)
    return list

test_list = ["Peter", "Bob", "Ana", "MARIO", "CEDRIC"]
remove_vowel_ending(test_list)
assert test_list == ["Peter", "Bob", "CEDRIC"]
assert remove_vowel_ending([]) == []