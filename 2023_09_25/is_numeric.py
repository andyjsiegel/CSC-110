def is_numeric(str):
    try: 
        int(str.replace(".", ""))
        return True
    except:
        return False

def main():
  print( is_numeric("234") ) # True
  print( is_numeric("abc") ) # False
  print( is_numeric("12c") ) # False
  print( is_numeric("12.3") ) # True
  print( is_numeric("1.2.3") ) # True

main()