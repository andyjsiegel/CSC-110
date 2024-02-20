def bubble_sort(items):
  end = len(items)-1
  for i in range(len(items)-1):
    for j in range(end):
      if items[j] > items[j+1]:
        items[j], items[j+1] = items[j+1], items[j]
    end -=1

def main():
  test_list = [5, 10, 20, 6, 7, 9, 43, 10, 12]
  bubble_sort(test_list)
  print(test_list)
  
main()