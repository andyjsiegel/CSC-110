def count_vowels(string):
    vowel_dict = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "A": 0, "E": 0, "I": 0, "O": 0, "U":0}
    for letter in string:
        try:
            vowel_dict.update({letter: vowel_dict[letter]+1})
        except KeyError:
            print("", end="")

    return vowel_dict

print( count_vowels("") ) # {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
                
print( count_vowels("banana") ) # {"a": 3, "e": 0, "i": 0, "o": 0, "u": 0, "A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
                                
print( count_vowels("Adriana") ) # {"a": 2, "e": 0, "i": 1, "o": 0, "u": 0, "A": 1, "E": 0, "I": 0, "O": 0, "U": 0}
                                 
print( count_vowels("Hello World!") ) # {"a": 0, "e": 1, "i": 0, "o": 2, "u": 0, "A": 0, "E": 0, "I": 0, "O": 0, "U": 0}

# All complete!