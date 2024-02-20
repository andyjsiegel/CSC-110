def total(file_name):
    f = open(f"./2023_12_14/{file_name}", 'r')
    sum = 0
    for line in f.readlines():
        sum += int(line.strip('\n'))
    return sum

print(total("data.txt"))