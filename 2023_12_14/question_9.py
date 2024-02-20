def sum_rows(two_d_list):
    for i in range(len(two_d_list)):
        if len(two_d_list[i]) > 0:
            sum = 0
            for number in two_d_list[i]:
                sum += number
            two_d_list[i] = round(sum/len(two_d_list[i]), 2)
        else:
            two_d_list[i] = None

    return two_d_list

print(sum_rows([[1.2, 5.4, 4.3, 2.0], [0.0, 1.0]]))
print(sum_rows([[], [10.5]]))
print(sum_rows([[1.0], [2.5, 3.5, 4.5], [0.0, 0.0], [0.0, 2.0]]))

assert sum_rows([[1.2, 5.4, 4.3, 2.0], [0.0, 1.0]]) == [3.23, 0.5]
assert sum_rows([[], [10.5]]) == [None, 10.5]
assert sum_rows([[1.0], [2.5, 3.5, 4.5], [0.0, 0.0], [0.0, 2.0]]) == [1, 3.5, 0.0, 1.0]