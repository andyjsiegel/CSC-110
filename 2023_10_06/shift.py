# TA's name is cole
# shift_right = lambda array: [None] + array[:-1] if array else []

def shift_right(items):
  index = len(items) - 1
  while index > 0:
    items[index] = items[index-1]
    index -= 1
  items[0] = None
  return items

