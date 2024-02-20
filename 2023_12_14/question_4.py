# def trim_ends(numbers):
#     for sublist in range(len(numbers)):
#         if len(numbers[sublist]) > 1:
#             numbers[sublist].pop(0)
#             numbers[sublist].pop(-1)
#         elif len(numbers[sublist]) == 1:
#             numbers[sublist].pop(0)

def trim_ends(lists):
    for sublist in lists:
        if len(sublist) > 0:
            sublist.pop(0)
        if len(sublist) > 0:
            sublist.pop(-1)



numbers = [ [10, 20, 200, 40],
[ ], [10],
[1000, 1000, 10],
[20, 30, 4, 100] ]
trim_ends(numbers)
assert numbers == [[20, 200], [ ], [ ], [1000], [30, 4]]