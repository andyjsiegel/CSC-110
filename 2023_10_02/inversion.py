def invert_dictionary(dictionary):
    thisdict = {}
    for x, y in dictionary.items():
        print(x,y)
        try:
            thisdict[y]
        except:
            if len(list(x)) > 0:
                thisdict[y] = list(x)
            else:
                thisdict[y] = ['']         
        else: 
            thisdict[y].append(x)
    return thisdict

