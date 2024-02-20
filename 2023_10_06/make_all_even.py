def make_all_even(integers):
    index = 0
    while index < len(integers):
        if integers[index] % 2 != 0:
            integers[index] += 1
        index += 1
    return integers

integers = [1,2,3,4]
print(make_all_even(integers))
print(integers)
    
