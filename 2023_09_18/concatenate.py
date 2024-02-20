def concatenate(words):
    i = 0
    string = ""
    while i < len(words):
       string = string + " " + words[i]
       i = i + 1
    return string[1:len(string)]


