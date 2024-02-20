# ta is cole
def count_vowels(string):
  counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
  for i in range(len(string)):
    char = string[i]
    if char in counts:
      counts[char] += 1
  return counts

def main():
  print( count_vowels("") ) # {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
  print( count_vowels("pineapple") ) # {"a": 1, "e": 2, "i": 1, "o": 0, "u": 0}
  
main()

# All complete!