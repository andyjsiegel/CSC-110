# my TA is cole
def merge_dictionaries(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] += dict2[key]
        else:
            dict1[key] = dict2[key]
    return dict1

def main():
  dict_1 = {"a": 20, "e": 5}
  dict_2 = {"e": 10, "i": 2}
  assert merge_dictionaries(dict_1, dict_2) == {"a": 20, "e": 15, "i": 2}
  print(dict_1)
  
main()