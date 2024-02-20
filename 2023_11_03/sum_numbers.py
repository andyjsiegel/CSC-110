# my TA is Cole
def sum_all(file_name):
    f = open(file_name, 'r')
    sum = 0
    for line in f.readlines():
        sum += int(line)
    f.close()
    return sum

