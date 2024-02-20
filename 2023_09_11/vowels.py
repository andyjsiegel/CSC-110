def count_vowels(str):
    i = 0
    vowels = 0
    while i < len(str):
        if str[i] in "aeiouAEIOU":
            vowels = vowels + 1
        i = i + 1
    return vowels


