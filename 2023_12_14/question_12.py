def remove_vowels(list):
    for i in range(len(list)):
        new_string = ""
        for char in list[i]:
            if char not in "aeiouAEIOU":
                new_string += char
        list[i] = new_string
    return list

test_list = ["Peter", "Bob", "Ana", "MARIO", "CEDRIC"]
remove_vowels(test_list)
print(test_list)
assert test_list == ["Ptr", "Bb", "n", "MR", "CDRC"]
assert remove_vowels([]) == []