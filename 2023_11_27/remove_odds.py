# My TA is cole
def remove_odds(lists_of_numbers):
  for sub_list in lists_of_numbers:
    for i in range(len(sub_list)-1, -1, -1): # Start at the end of the list, go backwards 1 step at a time to avoid index out of range error
      if sub_list[i] % 2 != 0:
        sub_list.pop(i)
  return lists_of_numbers

lists_of_numbers = [ [2, 3, 1, 2], [4, 5, 2, 1] ]
remove_odds(lists_of_numbers)
assert lists_of_numbers == [ [2, 2], [4, 2] ]