def reverse_string(str):
    count = len(str)-1
    reversed_string = ""
    while count <= len(str) and count >= 0:
        reversed_string = reversed_string + str[count]
        count = count-1

    return reversed_string

def remove_spaces(str):
    no_spaces = str.replace(" ", "")    
    return no_spaces

def is_palindrome(str):
    no_spaces_string = remove_spaces(str)
    reversed_string = reverse_string(no_spaces_string)
    if reversed_string == no_spaces_string:
        return True
    
    return False
