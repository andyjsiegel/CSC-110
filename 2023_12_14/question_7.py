def star_vowels(string):
    new_string = ""
    for char in string:
        if char in "aeiouAEIOU":
            new_string += "*"
        else:
            new_string += char

    return new_string

assert star_vowels("banana") == "b*n*n*"
assert star_vowels("a") == "*"
assert star_vowels("apple") == "*ppl*"
assert star_vowels("") == ""