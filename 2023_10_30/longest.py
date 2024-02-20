# Programming Problem 24
def longest_string(dictionarys):
    longest = None
    for dictionary in dictionarys:
        for value in dictionary.values():
            if longest == None or len(value) > len(longest):
                longest = value

    return longest

data = [{'a':'horse', 'b':'caterpillar'}, {'a':'camp', 'c':'joker'}]
print( longest_string(data) ) # caterpillar

data = [{1:'abc', 5:'onetwothree'}, {2:'abcd'}, {7:'one two three'}]
print( longest_string(data) ) # one two three

print( longest_string([]))

