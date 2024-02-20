# my TA is cole
def count_names(file_name):
    file_name = file_name
    f = open(file_name, 'r')
    my_list = []
    for item in f.readlines():
        if item.strip() != "":
            my_list.append(item.strip())
    return len(list(set(my_list)))
